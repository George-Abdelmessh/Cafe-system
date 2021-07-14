from DB import *
from tkinter import *

# Main page
" program main page object and responsive frame "
top = Tk()
top.state('zoomed')
top.config(bg='#282d3a')
top.title(f"Shop Name")
top.iconbitmap("photo/icon1.ico")
" get screen geometry to make it responsive "
screenwidth = top.winfo_screenmmwidth()
screenheight = top.winfo_screenheight()
top.geometry("%dx%d+0+0" % (screenwidth, screenheight))
top.minsize(1050, 700)


# operations to Create GUi
" operations to create new pages, Labels and buttons "
def createPage(tittle, width, height):
    global root
    root = Tk()
    root.title(tittle)
    root.minsize(width, height)


def createLabel(text="Label", pagename=top, fontsize=16):
    label = Label(pagename, text=text)
    label.config(font=("Courier", fontsize))
    label.pack()


def createButton(page=top, text="Button", command=0, fontsize=13):
    show = Button(page, text=text, command=command)
    show.config(font=("Courier", fontsize))
    show.pack()


# new page to add new product
#
def addProduct():
    createPage("Add", 300, 300)
    createLabel("Product Name", root, 16)
    nameentry = Entry(root)
    nameentry.config(font=("Courier", 13))
    nameentry.pack()
    createLabel("Product Price", root, 16)

    priceentry = Entry(root)
    priceentry.config(font=("Courier", 13))
    priceentry.pack()

    createLabel("Select Category", root, 16)
    value = IntVar()
    drinkstbut = Radiobutton(root, text="Drinks", variable=value, font=("Courier", 13),
                             value=0, command=lambda: value.set(0)).pack()
    dessertbut = Radiobutton(root, text="Desert", variable=value, font=("Courier", 13),
                             value=1, command=lambda: value.set(1)).pack()
    foodbut = Radiobutton(root, text="Food", variable=value, font=("Courier", 13),
                          value=2, command=lambda: value.set(2)).pack()

    def add():  # Add product to database
        if value.get() == 0:
            Product.addProduct(nameentry.get(), priceentry.get(), "Drinks")
            createLabel("Added Done", root, 16)
        elif value.get() == 1:
            Product.addProduct(nameentry.get(), priceentry.get(), "Dessert")
            createLabel("Added Done", root, 16)
        elif value.get() == 2:
            Product.addProduct(nameentry.get(), priceentry.get(), "Food")
            createLabel("Added Done", root, 16)
        else:
            createLabel("Error!", root, 16)

    createButton(root, "Add", add, 13)


# new page to show all data from database
def showall():
    createPage("Show All", 300, 300)
    result = Product.showAll()
    createLabel(result, root, 14)


# delete product from database
def deleteproduct():
    createPage("Delete Product", 300, 300)
    createLabel("Product ID", root, 14)
    identry = Entry(root)
    identry.config(font=("Courier", 13))
    identry.pack()

    def delete():
        Product.deleteProduct(identry.get())
        createLabel("Deleted", root, 13)

    createButton(root, "Delete", delete)


def modifyProduct():
    createPage("Modify Product", 300, 300)
    createLabel("Product ID", root, 14)
    identry = Entry(root)
    identry.config(font=("Courier", 13))
    identry.pack()

    createLabel("Product new Name", root, 14)
    nameentry = Entry(root)
    nameentry.config(font=("Courier", 13))
    nameentry.pack()

    createLabel("Product New Price", root, 14)
    priceentry = Entry(root)
    priceentry.config(font=("Courier", 13))
    priceentry.pack()

    createLabel("Select Category", root, 16)
    value = IntVar()
    drinkstbut = Radiobutton(root, text="Drinks", variable=value, font=("Courier", 13),
                             value=0, command=lambda: value.set(0)).pack()
    dessertbut = Radiobutton(root, text="Desert", variable=value, font=("Courier", 13),
                             value=1, command=lambda: value.set(1)).pack()
    foodbut = Radiobutton(root, text="Food", variable=value, font=("Courier", 13),
                          value=2, command=lambda: value.set(2)).pack()

    def modify():
        if value.get() == 0:
            Product.modifyProduct(identry.get(), nameentry.get(), priceentry.get(), "Drinks")
            createLabel("Updated", root, 13)
        elif value.get() == 1:
            Product.modifyProduct(identry.get(), nameentry.get(), priceentry.get(), "Dessert")
            createLabel("Updated", root, 13)
        elif value.get() == 2:
            Product.modifyProduct(identry.get(), nameentry.get(), priceentry.get(), "Food")
            createLabel("Updated", root, 13)
        else:
            createLabel("Error!", root, 13)

    createButton(root, "Update", modify, 13)


def showAProduct():
    createPage("Get A Product", 300, 300)
    createLabel("Product ID", root, 13)
    identry = Entry(root)
    identry.config(font=("Courier", 13))
    identry.pack()

    def show():
        result = Product.showAProduct(identry.get())
        createLabel(result, root, 13)

    createButton(root, "Show", show, 13)


def showProductsID():
    createPage("Get Product ID", 300, 300)
    createLabel("Product Name", root, 14)
    nameentry = Entry(root)
    nameentry.config(font=("Courier", 13))
    nameentry.pack()

    def showid():
        result = Product.showProductID(nameentry.get())
        createLabel(result, root, 16)

    createButton(root, "Show ID", showid, 13)


# operations menu
menu = Menu(top)
top.config(menu=menu)
operations = Menu(menu)
menu.add_cascade(label="Operations", menu=operations)
operations.add_command(label="Add Product", command=addProduct)
operations.add_command(label="Modify Product", command=modifyProduct)
operations.add_command(label="Delete Product", command=deleteproduct)
operations.add_separator()
operations.add_command(label="Show All Products", command=showall)
operations.add_command(label="Get A Product", command=showAProduct)
operations.add_command(label="Get Product ID", command=showProductsID)


# Frames functions
def drinksProducts():
    result = Product.showAllNames('Drinks')
    count = 0
    ypos = 20
    xpos = 20
    while count != len(result):
        Buttons(result[count], xpos, ypos, product)
        count += 1
        xpos += 80
        if xpos >= 900:
            xpos = 20
            ypos += 80


def Buttons(name, xpos, ypos, s):
    bb = name
    bb = Button(s, text=name, bg='#fe3943', width=6, height=3,
                font=("Courier", 13, 'bold'), bd=1, command=lambda: Product.selectPrice(name))
    bb.place(x=xpos, y=ypos)


# Receipt frame
receipt = Frame(top, width=533, bg='#171a1a')
receipt.pack(anchor=W, fill=Y, expand=False, side=RIGHT)


# Category frame
category = Frame(top, width=100, bg='#171a1a')
category.pack(anchor=W, fill=Y, expand=False, side=LEFT)

# products frame
product = Frame(top, width=900, bg='#282d3a')
product.pack(anchor=W, fill=Y, expand=False, side=LEFT)


def addCategory(name, ypostion, photo, command):
    button = Button(category, image=photo, bg='#171a1a', border=0, padx=0, pady=0,
                    anchor="center", command=command)
    button.place(x=15, y=ypostion)
    label = Label(category, text=name, bg='#171a1a', fg='white', font=('Courier', 12, 'bold'), anchor="center")
    label.place(x=12, y=ypostion + 60)


drinksimage = PhotoImage(file='photo/drink.png')
addCategory("Drinks", 30, drinksimage, drinksProducts)

dessertimage = PhotoImage(file='photo/dessert.png')
addCategory("Dessert", 130, dessertimage, '')

foodimage = PhotoImage(file='photo/food.png')
addCategory("Food", 230, foodimage, 'pass')


top.mainloop()
Product.saveClose()
