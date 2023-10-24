
class Cart():
    def __init__(self):
        self.shopping_cart = {}   
        self.item_list = 0 

    def addItem(self):
        item = input('Howdy, Welcome to Delilahs Den, What items would you like to add to your shopping cart?')
        item_price = (input(f' What  is the price of the {item} you added to your cart?'))
        self.shopping_cart[item] = item_price
        self.item_list += 1
        print( f'{item} was added to your shopping cart!')
        print(f' The items in your shopping cart are {self.shopping_cart}')

    def removeItem(self):
        item = input('Which item would you like to Remove from Cart')
        if(item in self.shopping_cart):
            del self.shopping_cart[item]
            self.item_list -= 1
            print (f'{item} has been removed from your shopping cart')
            print(f' These are the items that are currently in your cart {self.shopping_cart}')
        else:
            print(f'{item} is not in your current cart')


    def showCart(self):
        print(f' Current Cart Consists Of The Following Items {self.shopping_cart} .')
        print( '|-------- Check Out Items ---------|')
        for k, v in self.shopping_cart.items():
            print(k,v)

    def runner(self):
      while True:
          choice = input('Choose Your Poison! (add, remove, reveal or quit)').lower()
          if(choice =='quit'):
               print(f'Now Go On, Get!!')
               break
          elif (choice == 'add'):
               self.addItem()
          elif (choice == 'remove'):
               self.removeItem()
          elif (choice == 'reveal'):
               self.showCart()
          else:
               print('Youre making stuff up now, Try Again, Hurry Up & Buy...')

StevesDeli = Cart()
StevesDeli.addItem()
StevesDeli.addItem()
StevesDeli.removeItem()
StevesDeli.showCart()