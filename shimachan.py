import time
import random

class Shimaenaga():
    def __init__(self, name, color, size, kind):
        self.name = name
        self.color = color
        self.size = size
        self.kind = kind
        self.energy = 100
        self.hydration = 100
        self.food = []
        self.hunting_failure_count = 0
        self.places = ['tree', 'bush', 'hole', 'grass', 'swamp', 'field', 'forest']

    @property
    def is_alive(self):
        return self.energy > 0
    
    def energy_level(self):
        print(f'    Energy/Hydration: {round(self.energy,2)} / {round(self.hydration,2)}')

    def tweet(self):
        print(f'Trill trill trill! {self.name} is here!')
        self.energy = self.energy -1
        self.hydration = self.hydration - 5

        # There is a 5% of chance of being hunted while tweeting
        if random.random() < 0.05:
            self.being_hunted()

    def hunt(self):
        # self.places = ['tree', 'bush', 'hole', 'grass', 'swamp', 'field', 'forest']
        print(f'{self.name} is hunting!')
        
        # Player gets to choose where to hunt from the list of places
        print('Choose the place to hunt:')
        print('1. Swamp')
        print('2. Field')
        print('3. Forest')
        choice = input('Enter your choice: ')

        if choice == '1':
            place = 'swamp'
            # There is a 25% of chance of encountering a snake
            if random.random() < 0.25:
                print(f'{self.name} was caught by a snake! :(')
                self.energy = 0
            else:
                print(f'{self.name} caught a fish!')
                self.food.append('fish')
                self.energy = self.energy - 15
                self.hydration = self.hydration - 25

        elif choice == '2':
            place = 'field'
            # There is a 40% of chance of encountering a human
            if random.random() < 0.4:
                print(f'{self.name} was caught by a human! :(')
                self.energy = 0
            else:
                print(f'{self.name} caught a worm!')
                self.food.append('worm')
                self.energy = self.energy - 15
                self.hydration = self.hydration - 25

        elif choice == '3':
            place = 'forest'
            # There is a 20% of chance of encountering a cat
            if random.random() < 0.2:
                print(f'{self.name} was caught by a cat! :(')
                self.energy = 0
            else:
                print(f'{self.name} caught a bug!')
                self.food.append('bug')
                self.energy = self.energy - 15
                self.hydration = self.hydration - 25
        else:
            print('Invalid choice!')
            return
        



    # def hunt(self, prey):
    #     print(f'{self.name} is hunting {prey}!')
    #     # If hunting is successful
    #     if random.random() < 0.45:
    #         print(f'{self.name} caught {prey}!')
    #         self.food.append(prey)
    #         self.hunting_failure_count = 0
    #         self.eat()
    #     else:
    #         print(f'{self.name} failed to catch {prey}! :(')
    #         self.hunting_failure_count += 1
    #         if self.hunting_failure_count >= 3:
    #             print(f'{self.name} is tired and starves to death.')
    #             self.energy = 0
    #             return
    #     self.energy = self.energy - 15
    #     self.hydration = self.hydration - 25        

    def eat(self):
        if len(self.food) > 0:
            food = self.food.pop()
            print(f'{self.name} is eating {food}!')
        
            # This shouldn't be over 100
            self.energy = self.energy + 30
            self.hydration = self.hydration + 15
            if self.energy > 100:
                self.energy = 100
        else:
            print(f'{self.name} is hungry but does not have food :(')
            self.hunt()

    def drink(self):
        if random.random() < 0.1:
            print(f'{self.name} is drinking bad water! :(')
            self.energy = 10
            self.find_medical_help()
        else:
            print(f'{self.name} drank water!')
            self.hydration = 100
    
    def find_medical_help(self):
        print(f'{self.name} is looking for medical help!')
        if random.random() < 0.3:
            print(f'{self.name} found medical help!')
            self.energy = 100
            self.hydration = 100
        else:
            print(f'{self.name} could not find medical help and dies miserably! :(')
            self.energy = 0

    def poop(self):
        print(f'{self.name} pooped!')
        self.color = 'Brown'
        self.preen()
        
        
    def preen(self):
        print(f'{self.name} is preening!')
        self.color = 'White'
        self.energy = self.energy - 5
        self.hydration = self.hydration - 15
        

    def sleep(self):
        print(f'{self.name} is sleeping!')
        self.energy = 100

        # There is a 20% of chance of being hunted while sleeping
        if random.random() < 0.2:
            print(f'{self.name} is being hunted while sleeping!')
            if random.random() < 0.8:
                print(f'{self.name} is caught while sleeping! :(')
                self.energy = 0
            else:
                print(f'Phew! Predator thought {self.name} was dead and left!')
        

    # def being_hunted(self):
    #     print(f'{self.name} is being hunted!')
    #     if random.random() < 0.3:
    #         print(f'{self.name} escaped!')
    #         self.energy = self.energy - 20
    #         self.hydration = self.hydration - 30
    #     else:
    #         print(f'{self.name} was caught! :(')
    #         self.energy = 0

    def being_hunted(self):
        predator = random.choices(['Eagle', 'Snake', 'Cat', 'Owl', 'Human'], weights=[0.3, 0.2, 0.1, 0.4, 0.3])[0]

        action_choices = ['fight', 'flight', 'freeze', 'play_dead', 'hide']
        # Player gets to choose the action
        print(f'{self.name} is being hunted by {predator}!')
        print('Choose the action:')
        print('1. Fight')
        print('2. Flight')
        print('3. Freeze')
        print('4. Play Dead')
        print('5. Hide')
        choice = input('Enter your choice: ')

        if choice == '1':
            print(f'{self.name} is fighting {predator}!')
            if random.random() < 0.3:
                print(f'{self.name} won the fight!')
                self.energy = self.energy - 20
                self.hydration = self.hydration - 30
            else:
                print(f'{self.name} lost the fight! :(')
                self.energy = 0
        elif choice == '2':
            print(f'{self.name} is flying away from {predator}!')
            if random.random() < 0.3:
                print(f'{self.name} escaped!')
                self.energy = self.energy - 20
                self.hydration = self.hydration - 30
            else:
                print(f'{self.name} was caught! :(')
                self.energy = 0
        elif choice == '3':
            print(f'{self.name} is freezing!')
            if random.random() < 0.3:
                print(f'{self.name} escaped!')
                self.energy = self.energy - 20
                self.hydration = self.hydration - 30
            else:
                print(f'{self.name} was caught! :(')
                self.energy = 0
        elif choice == '4':
            print(f'{self.name} is playing dead!')
            if random.random() < 0.3:
                print(f'{self.name} escaped!')
                self.energy = self.energy - 20
                self.hydration = self.hydration - 30
            else:
                print(f'{self.name} was caught! :(')
                self.energy = 0
        elif choice == '5':
            
            place = random.choices(self.places, weights=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])[0]

            print(f'{self.name} is hiding in {place}!')
            if place == 'tree':
                # There is a 40% chance of encountering an owl or an eagle
                if random.random() < 0.4:
                    print(f'{self.name} was caught by an owl or an eagle! :(')
                    self.energy = 0
                else:
                    print(f'{self.name} escaped!')
                    self.energy = self.energy - 20
                    self.hydration = self.hydration - 30
            elif place == 'bush':
                # There is a 30% chance of encountering a snake
                random_number = random.random()
                if random_number < 0.3:
                    print(f'{self.name} was caught by a snake! :(')
                    self.energy = 0
                # There is a 30% chance of encountering a cat
                elif random_number < 0.6:
                    print(f'{self.name} was caught by a cat! :(')
                    self.energy = 0
                else:
                    print(f'{self.name} escaped!')
                    self.energy = self.energy - 20
                    self.hydration = self.hydration - 30
            elif place == 'hole':
                # There is a 20% chance of encountering a snake
                if random.random() < 0.2:
                    print(f'{self.name} was caught by a snake! :(')
                    self.energy = 0
                else:
                    print(f'{self.name} escaped!')
                    self.energy = self.energy - 20
                    self.hydration = self.hydration - 30
            elif place == 'grass':
                # There is a 10% chance of encountering a human
                if random.random() < 0.1:
                    print(f'{self.name} was caught by a human! :(')
                    self.energy = 0
                else:
                    print(f'{self.name} escaped!')
                    self.energy = self.energy - 20
                    self.hydration = self.hydration - 30
            

            

        else:
            print('Invalid choice!')



    def __str__(self):
        return f'{self.name} is {self.color} and {self.size} {self.kind} - Energy: {self.energy}'
    

    def random_events():
        shimachan = Shimaenaga(name='Shima-chan', color='White', size='Small', kind='Bird')
        print(shimachan)

        # evil_shimachan = Shimaenaga(name='Shima-kozo', color='Black', size='Large', kind='Bird')
        # print(evil_shimachan)

        wait_time = 2

        while shimachan.is_alive:

            # Randomize the action based on the weight
            weights = [0.8, 0.5, 0.5, 0.3, 0.6, 0.7, 0.1]
            action = random.choices(['tweet', 'poop', 'preen', 'sleep', 'hunt', 'eat', 'being_hunted'], weights=weights)[0]

            if action == 'tweet':
                shimachan.tweet()
            elif action == 'poop':
                shimachan.poop()
            elif action == 'preen':
                shimachan.preen()
            elif action == 'sleep':
                shimachan.sleep()
            elif action == 'hunt':
                shimachan.hunt()
            elif action == 'eat':
                shimachan.eat()
            elif action == 'being_hunted':
                shimachan.being_hunted()

            if shimachan.hydration <= 40:
                print('Shima-chan is thirsty!')
                shimachan.drink()
            
            shimachan.energy_level()
            time.sleep(wait_time)

        print('Shima-chan is dead :(')


def based_on_choice():
    # Player gets to choose the events. Prompt the player to choose the events.
    shimachan = Shimaenaga(name='Shima-chan', color='White', size='Small', kind='Bird')
    print(shimachan)
 
    wait_time = 2

    while shimachan.is_alive:
        print('Choose the event:')
        print('1. Tweet')
        print('2. Preen')
        print('3. Sleep')
        print('4. Hunt')
        print('5. Eat')
        print('6. Drink')
        print('7. Poop')
        print('8. Being Hunted')
        print('9. Random Events')
        print('0. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            shimachan.tweet()
        elif choice == '2':
            shimachan.preen()
        elif choice == '3':
            shimachan.sleep()
        elif choice == '4':
            shimachan.hunt()
        elif choice == '5':
            shimachan.eat()
        elif choice == '6':
            shimachan.drink()
        elif choice == '7':
            shimachan.poop()
        elif choice == '8':
            shimachan.being_hunted()
        elif choice == '9':
            Shimaenaga.random_events()
        elif choice == '0':
            break
        else:
            print('Invalid choice!')

        if shimachan.hydration <= 40:
            print('Shima-chan is thirsty!')
            shimachan.drink()
        
        shimachan.energy_level()
        time.sleep(wait_time)

if __name__ == '__main__':
    based_on_choice()

