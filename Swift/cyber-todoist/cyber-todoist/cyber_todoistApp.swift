import SwiftUI

@main
struct CyberpunkTasksApp: App {
    init() {
        setupWindowAppearance()
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(
                    minWidth: 300, maxWidth: 700,
                    minHeight: 300, maxHeight: 700)
        }
        .windowStyle(HiddenTitleBarWindowStyle()) // Optional: Hide title bar
        .windowResizability(.contentSize)
        .defaultSize(CGSize(width: 300, height: 700))
    }
}

// MARK: - Custom Window Styling
func setupWindowAppearance() {
    if let window = NSApplication.shared.windows.first {
        window.setContentSize(NSSize(width: 300, height: 700)) // ✅ Default window size
        window.titlebarAppearsTransparent = true               // Transparent title bar
        window.backgroundColor = NSColor.purple                // Set title bar colour
        window.isMovableByWindowBackground = true
    }
}
