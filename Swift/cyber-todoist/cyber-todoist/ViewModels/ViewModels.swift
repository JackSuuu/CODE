//
//  ViewModels.swift
//  cyber-todoist
//
//  Created by Jack on 2025/2/7.
//

// TaskViewModel.swift
import SwiftUI

class TaskViewModel: ObservableObject {
    @Published var tasks: [Task] = []

    func addTask(title: String) {
        guard !title.isEmpty else { return }
        tasks.append(Task(title: title))
    }

    func removeTask(at offsets: IndexSet) {
        tasks.remove(atOffsets: offsets)
    }


    func toggleCompletion(for task: Task) {
        if let index = tasks.firstIndex(where: { $0.id == task.id }) {
            tasks[index].isCompleted.toggle()
        }
    }
}
