import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# --- INITIALIZE MEMORY VAULT ---
if 'owner' not in st.session_state:
    st.session_state.owner = Owner("Izayah")
    
# Initialize the Scheduler
scheduler = Scheduler(st.session_state.owner)

st.title(f"🐾 PawPal+: {st.session_state.owner.name}'s Dashboard")
st.divider()

# --- SECTION 1: ADD A PET ---
st.header("🐶 Add a New Pet")
with st.form("add_pet_form"):
    col1, col2 = st.columns(2)
    with col1:
        pet_name = st.text_input("Pet Name")
    with col2:
        pet_species = st.selectbox("Species", ["Dog", "Cat", "Bird", "Other"])
    
    submit_pet = st.form_submit_button("Add Pet")
    if submit_pet and pet_name:
        new_pet = Pet(pet_name, pet_species)
        st.session_state.owner.add_pet(new_pet)
        st.success(f"{pet_name} the {pet_species} has been added!")

# --- SECTION 2: ADD A TASK ---
st.header("📋 Schedule a Task")
if not st.session_state.owner.pets:
    st.info("Please add a pet above before scheduling tasks.")
else:
    with st.form("add_task_form"):
        # Get list of pet names for the dropdown
        pet_names = [pet.name for pet in st.session_state.owner.pets]
        selected_pet_name = st.selectbox("Select Pet", pet_names)
        
        task_desc = st.text_input("Task Description (e.g., Morning Walk)")
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            task_time = st.time_input("Time").strftime("%H:%M")
        with col_t2:
            task_freq = st.selectbox("Frequency", ["Once", "Daily", "Weekly"])
            
        submit_task = st.form_submit_button("Add Task")
        if submit_task and task_desc:
            # Find the actual Pet object and add the task
            target_pet = st.session_state.owner.get_pet(selected_pet_name)
            if target_pet:
                target_pet.add_task(Task(task_desc, task_time, task_freq))
                st.success(f"Task '{task_desc}' scheduled for {selected_pet_name} at {task_time}!")

st.divider()

# --- SECTION 3: SMART SCHEDULE VIEW ---
st.header("📅 Today's Smart Schedule")

if st.button("Generate Schedule"):
    daily_tasks = scheduler.get_daily_schedule()
    
    if not daily_tasks:
        st.info("No tasks scheduled for today. You get to relax!")
    else:
        # 1. Run the Algorithm: Check for Conflicts
        conflicts = scheduler.check_conflicts(daily_tasks)
        for warning in conflicts:
            st.warning(warning)
            
        # 2. Display the sorted tasks
        st.write("### Task List (Sorted by Time)")
        
        # Format the data cleanly for Streamlit
        schedule_data = []
        for task in daily_tasks:
            # Find which pet this task belongs to for display purposes
            pet_owner_name = "Unknown"
            for pet in st.session_state.owner.pets:
                if task in pet.tasks:
                    pet_owner_name = pet.name
                    break
                    
            schedule_data.append({
                "Time": task.time,
                "Pet": pet_owner_name,
                "Task": task.description,
                "Frequency": task.frequency,
                "Status": "✅ Done" if task.is_complete else "⏳ Pending"
            })
            
        st.table(schedule_data)
