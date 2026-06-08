import SwiftUI

struct ContentView: View {
    @StateObject var viewModel = TaskViewModel()
    @State private var newTaskTitle = ""
    @State private var gradientPhase = 0.0
    @State private var hoveredTaskId: UUID?
    @State private var selectedTaskId: UUID?
    @FocusState private var isInputFocused: Bool
    
    func addTask() {
        guard !newTaskTitle.isEmpty else { return }
        withAnimation(.smooth) {
            viewModel.addTask(title: newTaskTitle)
            newTaskTitle = ""
        }
    }
    
    func deleteSelectedTask() {
        guard !isInputFocused else { return }
        guard let selectedId = selectedTaskId,
              let index = viewModel.tasks.firstIndex(where: { $0.id == selectedId }) else { return }
        withAnimation(.smooth) {
            viewModel.removeTask(at: IndexSet([index]))
            selectedTaskId = nil
        }
    }

    var body: some View {
        ZStack {
            // Animated gradient background
            LinearGradient(
                gradient: Gradient(colors: [.black, .purple.opacity(0.8), .black]),
                startPoint: .topLeading,
                endPoint: UnitPoint(x: cos(gradientPhase), y: sin(gradientPhase))
            )
            .animation(.linear(duration: 10).repeatForever(autoreverses: false), value: gradientPhase)
            .edgesIgnoringSafeArea(.all)
            .onAppear { gradientPhase = .pi * 2 }
            
            VStack(spacing: 20) {
                // Input field
                HStack {
                    TextField("", text: $newTaskTitle)
                        .placeholder(when: newTaskTitle.isEmpty) {
                            Text("Add task...")
                                .foregroundColor(.purple.opacity(0.5))
                        }
                        .textFieldStyle(.plain)
                        .padding(12)
                        .background(Color.black.opacity(0.3))
                        .cornerRadius(8)
                        .overlay(
                            RoundedRectangle(cornerRadius: 8)
                                .stroke(.purple.opacity(0.5), lineWidth: 1)
                        )
                        .foregroundColor(.white)
                        .font(.system(.body, design: .monospaced))
                        .focused($isInputFocused)
                        .onSubmit(addTask)
                        .onKeyPress(.return) {
                            addTask()
                            return .handled
                        }
                }
                .padding(.horizontal)
                
                // Task list
                ScrollView {
                    VStack(spacing: 8) {
                        ForEach(viewModel.tasks) { task in
                            HStack {
                                Text(task.title)
                                    .font(.system(.body, design: .monospaced))
                                    .foregroundColor(.white)
                                    .strikethrough(task.isCompleted, color: .purple)
                                
                                Spacer()
                                
                                // Complete Button
                                Button {
                                    withAnimation {
                                        viewModel.toggleCompletion(for: task)
                                    }
                                } label: {
                                    Image(systemName: task.isCompleted ? "checkmark.square" : "square")
                                        .foregroundColor(task.isCompleted ? .purple : .white)
                                }
                                .buttonStyle(.plain)
                                
                                // Delete Button
                                Button {
                                    if let index = viewModel.tasks.firstIndex(where: { $0.id == task.id }) {
                                        withAnimation {
                                            viewModel.removeTask(at: IndexSet([index]))
                                        }
                                    }
                                } label: {
                                    Image(systemName: "trash")
                                        .foregroundColor(.red)
                                        .opacity(hoveredTaskId == task.id ? 1 : 0.5)
                                }
                                .buttonStyle(.plain)
                            }
                            .padding(12)
                            .background(Color.black.opacity(0.3))
                            .cornerRadius(8)
                            .overlay(
                                RoundedRectangle(cornerRadius: 8)
                                    .strokeBorder(
                                        selectedTaskId == task.id ? Color.purple :
                                        hoveredTaskId == task.id ? Color.purple.opacity(0.5) : Color.purple.opacity(0.3),
                                        lineWidth: 1
                                    )
                            )
                            .onHover { hovering in
                                hoveredTaskId = hovering ? task.id : nil
                            }
                            .onTapGesture {
                                selectedTaskId = task.id
                            }
                            .scaleEffect(hoveredTaskId == task.id ? 1.02 : 1)
                            .animation(.smooth, value: hoveredTaskId)
                        }
                    }
                    .padding(.horizontal)
                }
            }
            .padding(.vertical)
        }
        .onKeyPress(.delete) {
            deleteSelectedTask()
            return .handled
        }
    }
}

extension View {
    func placeholder<Content: View>(
        when shouldShow: Bool,
        alignment: Alignment = .leading,
        @ViewBuilder placeholder: () -> Content
    ) -> some View {
        ZStack(alignment: alignment) {
            placeholder().opacity(shouldShow ? 1 : 0)
            self
        }
    }
}
