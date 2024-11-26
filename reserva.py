from tkinter import *
from tkinter import ttk

class TaxiBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reserva de Táxi")
        
        # Variáveis
        self.carType = IntVar()
        self.journeyType = IntVar()
        self.Standard = StringVar(value="100")  # Valores de exemplo
        self.PrimeSedan = StringVar(value="150")
        self.PremiumSedan = StringVar(value="200")

        # Criar UI
        self.create_book_frame()
        self.create_receipt_frame()
        self.create_button_frame()

    def create_book_frame(self):
        Book_Frame = Frame(self.root)
        Book_Frame.pack()

        # Seleção do Tipo de Carro
        self.chkStandard = Radiobutton(Book_Frame, text="Padrão", value=1, variable=self.carType,
                                        font=('arial', 14, 'bold'), command=self.selectCar)
        self.chkStandard.grid(row=0, column=0, sticky=W)
        self.txtStandard = Label(Book_Frame, font=('arial', 14, 'bold'), width=7,
                                 textvariable=self.Standard, bd=5, state=DISABLED, justify=RIGHT,
                                 bg="white", relief=SUNKEN)
        self.txtStandard.grid(row=0, column=1)

        self.chkPrimeSedan = Radiobutton(Book_Frame, text="Prime Sedan", value=2, variable=self.carType,
                                          font=('arial', 14, 'bold'), command=self.selectCar)
        self.chkPrimeSedan.grid(row=1, column=0, sticky=W)
        self.txtPrimeSedan = Label(Book_Frame, font=('arial', 14, 'bold'), width=7,
                                   textvariable=self.PrimeSedan, bd=5, state=DISABLED, justify=RIGHT,
                                   bg="white", relief=SUNKEN)
        self.txtPrimeSedan.grid(row=1, column=1)

        self.chkPremiumSedan = Radiobutton(Book_Frame, text="Premium Sedan", value=3, variable=self.carType,
                                            font=('arial', 14, 'bold'), command=self.selectCar)
        self.chkPremiumSedan.grid(row=2, column=0)
        self.txtPremiumSedan = Label(Book_Frame, font=('arial', 14, 'bold'), width=7,
                                     textvariable=self.PremiumSedan, bd=5, state=DISABLED, justify=RIGHT,
                                     bg="white", relief=SUNKEN)
        self.txtPremiumSedan.grid(row=2, column=1)

        # Seleção do Tipo de Viagem
        self.chkSingle = Radiobutton(Book_Frame, text="Única", value=1, variable=self.journeyType,
                                      font=('arial', 14, 'bold'))
        self.chkSingle.grid(row=0, column=2, sticky=W)
        self.chkReturn = Radiobutton(Book_Frame, text="Retorno", value=2, variable=self.journeyType,
                                      font=('arial', 14, 'bold'))
        self.chkReturn.grid(row=1, column=2, sticky=W)
        self.chkSpecialNeeds = Radiobutton(Book_Frame, text="Necessidades Especiais", value=3, variable=self.journeyType,
                                            font=('arial', 14, 'bold'))
        self.chkSpecialNeeds.grid(row=2, column=2, sticky=W)

    def create_receipt_frame(self):
        ReceiptFrame = Frame(self.root)
        ReceiptFrame.pack()

        self.txtReceipt1 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt1.grid(row=0, column=0, columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt2.grid(row=0, column=2, columnspan=2)

    def create_button_frame(self):
        ButtonFrame = Frame(self.root)
        ButtonFrame.pack()

        self.btnTotal = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2,
                               text='Total', command=self.calculate_total)
        self.btnTotal.grid(row=0, column=0)

        self.btnReceipt = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2,
                                 text='Recibo', command=self.print_receipt)
        self.btnReceipt.grid(row=0, column=1)

        self.btnReset = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2,
                               text='Resetar', command=self.reset_fields)
        self.btnReset.grid(row=0, column=2)

        self.btnExit = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2,
                              text='Sair', command=self.root.quit)
        self.btnExit.grid(row=0, column=3)

    def selectCar(self):
        """Habilita ou desabilita labels com base no tipo de carro selecionado."""
        if self.carType.get() == 1:
            self.txtStandard.config(state=NORMAL)
            self.txtPrimeSedan.config(state=DISABLED)
            self.txtPremiumSedan.config(state=DISABLED)
        elif self.carType.get() == 2:
            self.txtStandard.config(state=DISABLED)
            self.txtPrimeSedan.config(state=NORMAL)
            self.txtPremiumSedan.config(state=DISABLED)
        elif self.carType.get() == 3:
            self.txtStandard.config(state=DISABLED)
            self.txtPrimeSedan.config(state=DISABLED)
            self.txtPremiumSedan.config(state=NORMAL)

    def calculate_total(self):
        # Implementar a lógica para calcular o custo total
        pass

    def print_receipt(self):
        # Implementar a lógica para imprimir recibos
        pass

    def reset_fields(self):
        # Implementar a lógica para resetar todos os campos
        pass

# Execução principal
if __name__ == '__main__':
    root = Tk()
    app = TaxiBookingApp(root)
    root.mainloop()