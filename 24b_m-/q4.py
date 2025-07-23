import math

class Lesson:
    def __init__(self, course_id, hour, minute): #
        self.id_ = course_id #
        self.duration_ = 120 # Default duration is 120 minutes

        # Validate hour and minute, set to 8:30 if invalid
        if not (8 <= hour <= 18) or not (0 <= minute <= 59): # [cite: 53, 54]
            self.hour_ = 8
            self.minute_ = 30
        else:
            self.hour_ = hour #
            self.minute_ = minute #

    # Get and set methods are assumed to be implemented, no need to write them
    # For testing purposes, I'll add simple getters here
    def get_id(self):
        return self.id_

    def get_hour(self):
        return self.hour_

    def get_minute(self):
        return self.minute_

    def get_duration(self):
        return self.duration_

    def get_end_time_in_minutes(self):
        """Helper to calculate end time in minutes from start of day."""
        return (self.hour_ * 60 + self.minute_) + self.duration_

    def after(self, other): #
        if not isinstance(other, Lesson): #
            return None #

        # Calculate end time for self and other in minutes from start of day
        self_end_time = self.get_end_time_in_minutes()
        other_end_time = other.get_end_time_in_minutes()

        return self_end_time > other_end_time #

    def __str__(self):
        return (f"Lesson(ID: {self.id_}, Start: {self.hour_}:{self.minute_:02d}"
                f", Duration: {self.duration_} mins)")

class WeeklyPlan:
    def __init__(self):
        self.lessons_ = [] #

    def add_lesson(self, lesson):
        """Helper to add lessons for testing."""
        self.lessons_.append(lesson)

    def total_minutes(self, course_id): #
        total = 0
        for lesson in self.lessons_: #
            if lesson.get_id() == course_id: #
                total += lesson.get_duration() #
        return total #

    def most_later_lesson(self): #
        if not self.lessons_: #
            return None #

        latest_lesson = None
        max_end_time = -1

        for lesson in self.lessons_: #
            current_end_time = lesson.get_end_time_in_minutes()
            if current_end_time > max_end_time:
                max_end_time = current_end_time
                latest_lesson = lesson
        return latest_lesson #

    def popular_course(self): #
        if not self.lessons_: #
            return "None" #

        course_durations = {}
        for lesson in self.lessons_: #
            course_id = lesson.get_id() #
            duration = lesson.get_duration() #
            course_durations[course_id] = course_durations.get(course_id, 0) + duration

        most_popular_id = None
        max_total_duration = -1

        for course_id, total_duration in course_durations.items():
            if total_duration > max_total_duration:
                max_total_duration = total_duration
                most_popular_id = course_id
        return most_popular_id #


# --- Test Cases ---

print("--- Testing Lesson Class ---")
# Part A: Constructor tests
lesson1 = Lesson("CS101", 10, 0)
print(f"Lesson 1: {lesson1} (Expected: ID: CS101, Start: 10:00, Duration: 120)")
lesson2 = Lesson("MATH202", 7, 0) # Invalid hour
print(f"Lesson 2: {lesson2} (Expected: ID: MATH202, Start: 8:30, Duration: 120)")
lesson3 = Lesson("PHY303", 15, 65) # Invalid minute
print(f"Lesson 3: {lesson3} (Expected: ID: PHY303, Start: 8:30, Duration: 120)")
lesson4 = Lesson("ART404", 18, 59) # Valid edge case
print(f"Lesson 4: {lesson4} (Expected: ID: ART404, Start: 18:59, Duration: 120)")


# Part B: after method tests
print("\n--- Testing Lesson.after method ---")
lessonA = Lesson("A", 9, 0) # Ends at 11:00 (660 mins)
lessonB = Lesson("B", 10, 0) # Ends at 12:00 (720 mins)
lessonC = Lesson("C", 9, 0) # Ends at 11:00 (660 mins)

print(f"Is LessonA after LessonB? {lessonA.after(lessonB)} (Expected: False)")
print(f"Is LessonB after LessonA? {lessonB.after(lessonA)} (Expected: True)")
print(f"Is LessonA after LessonC? {lessonA.after(lessonC)} (Expected: False)") # Ends at same time
print(f"Is LessonB after None? {lessonB.after(None)} (Expected: None)")
print(f"Is LessonB after 'string'? {lessonB.after('string')} (Expected: None)")

# Create lessons for WeeklyPlan tests
lesson_wp1 = Lesson("CS101", 9, 0)   # 120 min, ends 11:00
lesson_wp2 = Lesson("MATH202", 10, 30) # 120 min, ends 12:30
lesson_wp3 = Lesson("CS101", 14, 0)  # 120 min, ends 16:00
lesson_wp4 = Lesson("PHY303", 11, 0) # 120 min, ends 13:00
lesson_wp5 = Lesson("CS101", 16, 0)  # 120 min, ends 18:00
lesson_wp6 = Lesson("MATH202", 17, 0) # 120 min, ends 19:00 (latest)


print("\n--- Testing WeeklyPlan Class ---")
# Part C: total_minutes method
wp1 = WeeklyPlan()
wp1.add_lesson(lesson_wp1)
wp1.add_lesson(lesson_wp2)
wp1.add_lesson(lesson_wp3)
wp1.add_lesson(lesson_wp4)
wp1.add_lesson(lesson_wp5)
wp1.add_lesson(lesson_wp6)

print(f"Total minutes for CS101: {wp1.total_minutes('CS101')} (Expected: 360)") # 3 * 120
print(f"Total minutes for MATH202: {wp1.total_minutes('MATH202')} (Expected: 240)") # 2 * 120
print(f"Total minutes for PHY303: {wp1.total_minutes('PHY303')} (Expected: 120)") # 1 * 120
print(f"Total minutes for NonExistent: {wp1.total_minutes('NonExistent')} (Expected: 0)")

# Part D: most_later_lesson method
print("\n--- Testing WeeklyPlan.most_later_lesson method ---")
later_lesson = wp1.most_later_lesson()
print(f"Most later lesson: {later_lesson} (Expected: Lesson(ID: MATH202, Start: 17:00, Duration: 120 mins))")

wp_empty = WeeklyPlan()
print(f"Most later lesson in empty plan: {wp_empty.most_later_lesson()} (Expected: None)")

# Part E: popular_course method
print("\n--- Testing WeeklyPlan.popular_course method ---")
popular_course_id = wp1.popular_course()
print(f"Most popular course: {popular_course_id} (Expected: CS101)")

wp_empty_popular = WeeklyPlan()
print(f"Most popular course in empty plan: {wp_empty_popular.popular_course()} (Expected: None)")

# Test with courses having same total duration
wp_tie = WeeklyPlan()
wp_tie.add_lesson(Lesson("A", 9, 0)) # 120
wp_tie.add_lesson(Lesson("B", 10, 0)) # 120
print(f"Most popular course (tie): {wp_tie.popular_course()} (Expected: A or B, problem states 'one such course')")