//
//  Task.swift
//  cyber-todoist
//
//  Created by Jack on 2025/2/7.
//

// Task.swift
import Foundation

struct Task: Identifiable {
    var id = UUID()
    var title: String
    var isCompleted: Bool = false
}

