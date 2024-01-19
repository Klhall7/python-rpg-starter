class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.alive_status = self.check_alive_status()
                
    def check_alive_status(self): #allows me to check alive stat throughout the game
        print("a")
        return self.health > 0  #alive if health is above 0 #in respective hero and goblin class

    def attack(self): #attack defined within each subclass
        pass 
    
    def print_status(self): #prints current instance
        #print(f"You have {self.health} health {self.power} and power.")
        #print(f"You are a {self.__class__.__name__}") #overridden by current character in loop
        print(f"The {self.__class__.__name__} has {self.health} health and {self.power} power.")
        print(" ")

    #def print_status(self, enemy): #enemy makes parameter flexible 
        #print (f"You have {self.health}  health and {self.power} power.")
        #print (f"{enemy.__class__.__name__} has {enemy_health}  health and {enemy_power} power.")
        #enemy refers to whatever instance is the current enemy
        #__class__ is object attribute refers to class of "enemy" 
        #__name__ is attribute of object class of "enemy"; takes name of class as a string
        
    def get_attribute(self, attribute_name, default=None): 
        #none will give error if an attribute reference isn't defined
        return getattr(self, attribute_name, default)
        #getattr function is used to dynamically access the value of an attribute from an object; used on health & power 
        
class Hero(Character):
    def __init__(self, hero_health = 10, hero_power = 5):
        super().__init__(hero_health, hero_power)
        
        
    def attack(self, enemy): #current self attacks current enemy(goblin)
        print(f"Hero attacks {enemy.__class__.__name__}")
        enemy.health -= self.power 
        print(f"You do {self.power} damage to the {enemy.__class__.__name__}")
        self.check_alive_status()  # Update alive status
        
        
    def print_status(self):
        super().print_status() #inherit from Character
        pass
        
    def get_hero_health(self):
        return self.get_attribute('power') #will dynamically access hero's current power
    
    def get_hero_health(self):
        return self.get_attribute('health') #will dynamically access hero's current health
    
class Goblin(Character):
    def __init__(self, goblin_health = 6, goblin_power = 2):
        super().__init__(goblin_health, goblin_power)
        
        
    def attack(self, enemy): #current self attacks current enemy(hero)
        print(f"Goblin attacks {enemy.__class__.__name__}")
        enemy.health -= self.power
        print(f"The {enemy.__class__.__name__} does {enemy.power} damage to you")
        self.check_alive_status()  # Update alive status
        
        
    def print_status(self):
        super().print_status()
        pass
        
    def get_goblin_power(self): #dynamically access goblin's power
        return self.get_attribute('power')
    
    def get_goblin_health(self): #dynamically access goblin's health
        return self.get_attribute('health')
        
def main (): #centralize the attribute retrieval within the Character class.

    hero_health = 10 #health and power presets for subclasses
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    
    hero = Hero(hero_health, hero_power) #define attribute (x_x) for loop; X.X is for variable
    goblin = Goblin(goblin_health, goblin_power) 
    
    while goblin.health > 0 and hero.health > 0: 
        current_character = hero # Start with the Hero as the current character
        enemy = goblin #start with Goblin as enemy
        print()
        print(f"You are a {current_character.__class__.__name__}")
        current_character.print_status() #Loop starts with current character and prints status
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
    
        if user_input == "1":
            current_character.attack(enemy) #attack
            print("e")
            enemy.print_status()
            
        elif user_input == "2": 
            print("You choose to do nothing.")
            enemy.attack(current_character)
            current_character.print_status()
            
        elif user_input == "3":
            print("Goodbye.")
            break 
        
        else:
            print (f"Invalid input {user_input}") #control user input
            
        if not enemy.check_alive_status():
                print(f"You beat the {enemy.__class__.__name__}!")
                break
                
        if not current_character.check_alive_status():
                print(f"{enemy.__class__.__name__} killed you :/.")
                break
                
        enemy_power = current_character.get_attribute('power') #Call get_attributes
        enemy_health = current_character.get_attribute('health')
      
main() 


#THOUGHT TO ADD ON: 
            #print("Want to try again?")
            #print("4. Yes!")
            #print("5. No")
            #user_input = input()
            #if user_input == "4":
                 #reset 
            #if user_input == "5":
                #print("Goodbye.")
                #break 
            #else:
            #print (f"Invalid input {user_input}") #control user input