# Elfar Snær Arnarson
# 13 Janúar 2020
# Skilaverkefni 1
import csv

invoices = []

class Invoice:

    def __init__(self, partNumber, partDescription, quantity, pricePerItem):
        self.partNumber = partNumber
        self.partDescription = partDescription
        self.quantity = quantity
        self.pricePerItem = pricePerItem

    def getInvoiceAmount(self):
        return self.quantity * self.pricePerItem

    def printInvoice(self):
        print(f"Partnumber: {self.partNumber}\nPart Description: {self.partDescription}\n"
              f"Quantity: {self.quantity}\nPrice Per Item: {self.pricePerItem}")

    def openFile(self):
        file = None
        try:
            file = open("invoice.csv", "r", newline="\r\n", encoding="utf-8")
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                invoice = Invoice(row[0], row[1], row[2], row[3])
                invoices.append(invoice)
        except IOError:
            print("An error occured trying to read the file.")
        finally:
            print("Finished")
            if (file != None):
                file.close()

    def writeFile(self):
        file = None
        try:
            file = open("invoice.csv", "w", newline="", encoding="utf-8")
            for invoice in invoices:
                line = invoice.partNumber + ";" + invoice.partDescription + ";" + invoice.quantity + ";" + \
                       invoice.pricePerItem + "\r\n"
                file.write(line)
        except IOError:
            print("An error occured trying to read the file.")
        finally:
            print("Finished")
            if file != None:
                file.close()

    def addInvoice(self):
        number = input("Partnumber: ")
        description = input("Description: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        invoice = Invoice(number, description, quantity, price)
        invoices.append(invoice)

    def printInvoices(self):
        for invoice in invoices:
            invoice.printInvoice()

        # def readFile(self):
        """listi = []
        csv = open("invoice.csv", 'r')
        for line in csv:
            listi.append(line.strip("\n"))
        return listi"""

invoice = Invoice

invoice.openFile(invoice)
#invoice.addInvoice(invoice)
invoice.printInvoices(invoice)
#invoice.writeFile(invoice)