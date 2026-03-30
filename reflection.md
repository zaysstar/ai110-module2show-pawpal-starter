# PawPal+ Project Reflection

## 1. System Design

**Core Actions:**
1. Add a new pet to the owner's profile.
2. Schedule a recurring or one-time task (like feeding or a walk) for a specific pet.
3. View the daily schedule of all tasks across all pets, sorted by time.

**a. Initial design**
I designed the system using four primary classes to separate concerns effectively:
* **Task:** Acts as a data container holding the description, time, frequency, and completion status of a specific activity.
* **Pet:** Represents an individual animal, storing its name, species, and a dedicated list of its own `Task` objects.
* **Owner:** Acts as the main user profile, holding a name and managing a list of `Pet` objects.
* **Scheduler:** The "brain" of the operation. It takes in an `Owner` object and handles the complex logic of aggregating all tasks from all pets, sorting them by time, and checking for scheduling conflicts.

classDiagram
    class Task {
        +String description
        +String time
        +String frequency
        +Boolean is_complete
        +mark_complete()
        +update_time()
    }

    class Pet {
        +String name
        +String species
        +List~Task~ tasks
        +add_task(task)
        +get_pending_tasks()
        +get_all_tasks()
    }

    class Owner {
        +String name
        +List~Pet~ pets
        +add_pet(pet)
        +get_pet(name)
        +get_all_tasks()
    }

    class Scheduler {
        +Owner owner
        +get_daily_schedule()
        +sort_by_time()
        +check_conflicts()
        +filter_tasks(status, pet_name)
    }

    Owner "1" *-- "*" Pet : owns
    Pet "1" *-- "*" Task : has
    Scheduler --> "1" Owner : manages

**b. Design changes**
Based on AI feedback during the scaffolding phase, I decided to implement `Task` and `Pet` using Python's `@dataclass` decorator. Since these classes primarily exist to hold state (data) rather than execute complex independent logic, using dataclasses significantly reduces boilerplate `__init__` code and makes the architecture cleaner and more readable.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**
My scheduler primarily considers **time** as the main constraint. The logic ensures that when a user views their daily schedule, the tasks are sorted chronologically. I also implemented a constraint for **conflict detection**, which flags if multiple tasks are scheduled at the exact same time. I prioritized these because chronological order is the most fundamental requirement for any daily planner, and preventing double-booking is the first step toward "smart" scheduling.

**b. Tradeoffs**
One major tradeoff in my current `Scheduler` is how it handles conflicts. Right now, the algorithm only checks for *exact time matches* (e.g., two tasks at exactly 10:00). It does not account for task *duration* (e.g., a 60-minute walk starting at 10:00 overlapping with a feeding at 10:30). This tradeoff is reasonable for this scenario because it keeps the baseline logic lightweight and functional for a prototype, avoiding the complex datetime math required for full overlap detection.

---

## 3. AI Collaboration

**a. How you used AI**
I used AI extensively as a "co-pilot" for scaffolding and bridging systems. I used it to generate the initial Mermaid.js UML diagram to visualize the architecture, draft the Python `@dataclass` skeletons, and figure out how to navigate Streamlit's `st.session_state` so my `Owner` data wouldn't wipe out on every page refresh. The most helpful prompts were specific, context-bound requests, such as asking exactly how to write a lambda function to sort my "HH:MM" time strings.

**b. Judgment and verification**
During the implementation of Phase 4 (Algorithms), I pasted my code to the AI and it accidentally output a class with two identical `get_daily_schedule` methods—one from Phase 2 and the new one for Phase 4. Instead of blindly accepting the output, I had to evaluate the structure, recognize that Python would just overwrite the first method (leaving messy, redundant code), and ensure the old method was cleanly deleted so the new sorting logic took over properly.

---

## 4. Testing and Verification

**a. What you tested**
I tested four core behaviors using `pytest`:
1. **State changes:** Verifying `mark_complete()` correctly flips the boolean.
2. **Object relationships:** Verifying that adding a `Task` to a `Pet` actually increases the pet's task array length.
3. **Sorting:** Verifying the `Scheduler` orders an unsorted list of tasks chronologically.
4. **Conflicts:** Verifying the `Scheduler` correctly generates warning strings when given duplicate times.
These tests were critical because Streamlit UIs can be difficult to debug. By proving the core "brain" of the app works in isolation, I knew any bugs in the browser were purely UI issues, not logic failures.

**b. Confidence**
I am highly confident (5/5) in the current iteration of the logic. If I had more time, the next edge cases I would test are: tasks scheduled exactly at midnight ("00:00"), adding a pet with no tasks to ensure the scheduler doesn't crash on an empty list, and testing the recurrence logic across month boundaries (e.g., a daily task on February 28th).

---

## 5. Reflection

**a. What went well**
I am most satisfied with successfully bridging the gap between standard Python backend logic and the Streamlit frontend. Getting the object-oriented `Owner`, `Pet`, and `Task` instances to persist in Streamlit's memory vault (`st.session_state`) was a huge win that made the app feel like a real piece of software.

**b. What you would improve**
In the next iteration, I would implement a Priority system (High, Medium, Low) and add task durations. The scheduler would then be able to organize tasks not just chronologically, but by urgency, while accurately preventing overlapping time blocks.

**c. Key takeaway**
My biggest takeaway as a "lead architect" collaborating with AI is that while AI is incredibly fast at generating boilerplate code and UI layouts, it cannot manage the overall system state for you. I still had to orchestrate how the pieces fit together and act as the gatekeeper to ensure redundant code didn't slip into the final product.