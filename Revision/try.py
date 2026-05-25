import datetime


class LibraryItem:
    """Base class for all items in the library."""
    LIBRARY_NAME = "Central City Library"  # Class Attribute

    def __init__(self, title, creator, item_id):
        self.title = title
        self.creator = creator
        self.item_id = item_id
        self.is_checked_out = False
        self.due_date = None

    def calculate_fine(self, days_overdue):
        """Standard fine calculation."""
        return days_overdue * 0.50

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"[{self.item_id}] {self.title} by {self.creator} - ({status})"


class Book(LibraryItem):
    """Inheritance: Book is a specialized LibraryItem."""

    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.pages = pages

    def calculate_fine(self, days_overdue):
        # Books have a higher fine
        return days_overdue * 0.75


class Magazine(LibraryItem):
    """Inheritance: Magazine is a specialized LibraryItem."""

    def __init__(self, title, issue_date, item_id):
        super().__init__(title, "Various Authors", item_id)
        self.issue_date = issue_date


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_items = []

    def borrow(self, item):
        # ASSERT: Use for internal logic check (Programmer assumption)
        assert isinstance(item, LibraryItem), "Must be a LibraryItem instance!"

        if item.is_checked_out:
            print(f"Sorry, {item.title} is already taken.")
            return False

        item.is_checked_out = True
        self.borrowed_items.append(item)
        print(f"{self.name} successfully borrowed {item.title}.")
        return True


class LibrarySystem:
    def __init__(self):
        self.inventory = {}
        self.members = {}

    def add_item(self, item):
        self.inventory[item.item_id] = item

    def add_member(self, member):
        self.members[member.member_id] = member

    def generate_report(self):
        print(f"\n--- {LibraryItem.LIBRARY_NAME} REPORT ---")
        print(f"Total Items: {len(self.inventory)}")
        for item in self.inventory.values():
            print(item)
        print("---------------------------------------\n")


# --- SIMULATING PROGRAM EXECUTION ---

def main():
    # 1. Initialize System
    system = LibrarySystem()

    # 2. Create Items (OOP Objects)
    b1 = Book("Python Crash Course", "Eric Matthes", "B101", 544)
    b2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "B102", 180)
    m1 = Magazine("National Geographic", "Jan 2024", "M501")

    # 3. Add to inventory
    system.add_item(b1)
    system.add_item(b2)
    system.add_item(m1)

    # 4. Create Members
    alice = LibraryMember("Alice Smith", "USR01")
    bob = LibraryMember("Bob Jones", "USR02")
    system.add_member(alice)
    system.add_member(bob)

    # 5. Logic Operations
    print("Action Log:")
    alice.borrow(b1)
    bob.borrow(b1)  # Should fail as Alice has it
    bob.borrow(m1)

    # 6. View Report
    system.generate_report()

    # 7. Demonstrate Attribute Check
    print(f"Updating Library Name for all items...")
    LibraryItem.LIBRARY_NAME = "Global Knowledge Hub"
    system.generate_report()


if __name__ == "__main__":
    main()

# --- CODE EXPLANATION ---
# 1. Classes/Objects: Everything is an object (LibraryItem, Member, etc.)
# 2. Inheritance: Book and Magazine 'inherit' properties from LibraryItem.
# 3. Class Attribute: LIBRARY_NAME is shared by every instance.
# 4. Assertion: Inside LibraryMember.borrow(), we assert the input type.
# 5. Encapsulation: Logic for fine calculation stays inside the classes.
