Feature: Task list
   Scenario: Adding a task
       Given the To-Do list is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"
  