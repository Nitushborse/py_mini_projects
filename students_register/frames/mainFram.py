from customtkinter import CTkFrame, CTkToplevel, CTkLabel, CTkFrame
from tkinter import ttk
from utils.conponets import AppButton, AppEntry, center_window
from database.db import add_student, get_all_students, update_student, delete_student


class MainFram(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(width=1000, height=600, fg_color="#0f172a")
        self.pack_propagate(False)


        # ✅ Add Student Button
        self.add_btn = AppButton(self, text="Add Student", command=self.open_add_student_form)
        self.add_btn.pack(pady=10)

        # ✅ Treeview for Students
        self.tree = ttk.Treeview(
            self,
            columns=("roll", "name", "class", "city", "actions"),
            show="headings",
            height=15
        )

        # Column Headings
        self.tree.heading("roll", text="Roll No")
        self.tree.heading("name", text="Name")
        self.tree.heading("class", text="Class")
        self.tree.heading("city", text="City")
        self.tree.heading("actions", text="Actions")

        # Column Widths
        self.tree.column("roll", width=80, anchor="center")
        self.tree.column("name", width=200, anchor="center")
        self.tree.column("class", width=100, anchor="center")
        self.tree.column("city", width=150, anchor="center")
        self.tree.column("actions", width=150, anchor="center")

        # Style Treeview (Dark Theme)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#1a1a1a",
            foreground="white",
            rowheight=25,
            fieldbackground="#0f172a",
            bordercolor="#1f538d",
            borderwidth=1
        )
        style.map("Treeview", background=[("selected", "#1f538d")])

        self.tree.pack(pady=10)

        # ✅ Load Students from Database
        self.load_students()

        # ✅ Bind click event for Update/Delete
        self.tree.bind("<Button-1>", self.on_tree_click)


    # ✅ Load Students from Database
    def load_students(self):
        self.tree.delete(*self.tree.get_children())
        students = get_all_students()
        for stu in students:
            self.tree.insert("", "end", values=(stu[0], stu[1], stu[2], stu[3], "Update | Delete"))

    # ✅ Open Add Student Pop-up Form
    def open_add_student_form(self):
        form = CTkToplevel(self)
        form.title("Add New Student")
        center_window(form, 400, 350)
        form.configure(fg_color="#0f172a")
        form.resizable(False, False)

        # Entry Fields
        self.roll_entry = AppEntry(form, placeholder="Enter Roll No")
        self.roll_entry.pack(pady=10)

        self.name_entry = AppEntry(form, placeholder="Enter Name")
        self.name_entry.pack(pady=10)

        self.class_entry = AppEntry(form, placeholder="Enter Class")
        self.class_entry.pack(pady=10)

        self.city_entry = AppEntry(form, placeholder="Enter City")
        self.city_entry.pack(pady=10)

        # Save Button
        AppButton(form, text="Save", command=lambda: self.save_student(form)).pack(pady=20)

    # ✅ Save Student to Database & Treeview
    def save_student(self, form):
        roll = self.roll_entry.get()
        name = self.name_entry.get()
        class_ = self.class_entry.get()
        city = self.city_entry.get()

        if roll and name and class_ and city:
            add_student(roll, name, class_, city)
            self.load_students()  # reload from DB
            form.destroy()  # Close the pop-up after saving

    # ✅ Detect Click on Update/Delete
    def on_tree_click(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if region != "cell":
            return

        row_id = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)
        if not row_id:
            return

        col_index = int(column.replace("#", "")) - 1  # column index
        values = self.tree.item(row_id, "values")

        # Check if clicked on "Actions" column
        if col_index == 4:  # 0-based index, actions column is 4
            x_offset = self.tree.bbox(row_id, column)[0]
            click_x = event.x - x_offset

            if click_x < 70:  # Approx first half -> Update
                self.update_student(row_id, values)
            else:  # Second half -> Delete
                self.delete_student(row_id, values)

    # ✅ Update Student Pop-up
    def update_student(self, row_id, values):
        form = CTkToplevel(self)
        form.title("Update Student")
        # form.geometry("400x350")
        center_window(form,400,350)
        form.configure(fg_color="#0f172a")
        form.resizable(False, False)

        roll_entry = AppEntry(form, placeholder="Enter Roll No")
        roll_entry.insert(0, values[0])
        roll_entry.pack(pady=10)

        name_entry = AppEntry(form, placeholder="Enter Name")
        name_entry.insert(0, values[1])
        name_entry.pack(pady=10)

        class_entry = AppEntry(form, placeholder="Enter Class")
        class_entry.insert(0, values[2])
        class_entry.pack(pady=10)

        city_entry = AppEntry(form, placeholder="Enter City")
        city_entry.insert(0, values[3])
        city_entry.pack(pady=10)

        AppButton(
            form,
            text="Update",
            command=lambda: self.save_updated_student(form, row_id, roll_entry, name_entry, class_entry, city_entry)
        ).pack(pady=20)

    def save_updated_student(self, form, row_id, roll_entry, name_entry, class_entry, city_entry):
        roll = roll_entry.get()
        name = name_entry.get()
        class_ = class_entry.get()
        city = city_entry.get()

        update_student(roll, name, class_, city)
        self.load_students()
        form.destroy()

    # ✅ Dark-Themed Delete Confirmation
    def delete_student(self, row_id, values):
        confirm_window = CTkToplevel(self)
        confirm_window.title("Confirm Delete")
        # confirm_window.geometry("300x150")
        center_window(confirm_window,300,150)
        confirm_window.configure(fg_color="#0f172a")
        confirm_window.resizable(False, False)

        # Center text
        CTkLabel(
            confirm_window,
            text=f"Delete student '{values[1]}'?",
            font=("Arial", 14),
            text_color="white"
        ).pack(pady=20)

        # Buttons Frame
        btn_frame = CTkFrame(confirm_window, fg_color="#0f172a")
        btn_frame.pack(pady=10)

        # Yes Button (Delete)
        AppButton(
            btn_frame,
            text="Yes",
            command=lambda: self.confirm_delete(confirm_window, row_id)
        ).pack(side="left", padx=10)

        # No Button (Cancel)
        AppButton(
            btn_frame,
            text="No",
            command=confirm_window.destroy
        ).pack(side="left", padx=10)

    def confirm_delete(self, confirm_window, row_id):
        roll = self.tree.item(row_id, "values")[0]
        delete_student(roll)
        self.load_students()
        confirm_window.destroy()

