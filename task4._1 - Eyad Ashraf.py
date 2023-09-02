import random


class Villain:
    def __init__(self, name, health=100, energy=500, shield=None,weapon=None):
        self.name = name
        self.health = health
        self.energy = energy
        self.shield = shield
        self.weapon = weapon

    def choose_Weapon(self):
        raise NotImplementedError("Subclasses must implement choose_action method.")

    def choose_Shield(self):
        raise NotImplementedError("Subclasses must implement choose_action method.")

    def take_damage(self, damage):
        self.health -= self.shield.damage_reduction*damage

    def use_energy(self, energy):
        self.energy -= energy

    def apply_shield(self, shield):
        self.shield = shield

    def reset_shield(self):
        self.shield = 1

    def is_alive(self):
        return self.health > 0


class Gru(Villain):
    def choose_Weapon(self,chosenWeapon):
        self.weapon = chosenWeapon
        return self.weapon
    def choose_Shield(self,chosenShield):
        self.shield = chosenShield
        return self.shield


class Vector(Villain):
    def choose_Weapon(self,chosenWeapon):
        self.weapon = chosenWeapon
        return self.weapon
    def choose_Shield(self,chosenShield):
        self.shield = chosenShield
        return self.shield


class GruWeapons:
    energy = None
    damage = None
    resources = None
    description = None

    def __str__(self):
        return self.__class__.__name__


class FreezeGun(GruWeapons):
    energy = 50
    damage = 11
    resources = "Inf"
    description = "Minions occasionally wield freeze ray guns that shoot a freezing beam to immobilize opponents temporarily."


class ElectricProd(GruWeapons):
    energy = 88
    damage = 18
    resources = 5
    description = "Minions might use electric prods to deliver mild shocks to enemies, stunning them momentarily."


class MegaMagnet(GruWeapons):
    energy = 92
    damage = 10
    resources = 3
    description = "Minions utilize a mega magnet to attract or repel metal objects, potentially disrupting enemy vehicles or equipment."


class KalmanMissile(GruWeapons):
    energy = 120
    damage = 20
    resources = 1
    description = "This unavoidable Missile created for enourmous distraction"


class VectorWeapons:
    energy = None
    damage = None
    resources = None
    description = None

    def __str__(self):
        return self.__class__.__name__


class LaserBlasters(VectorWeapons):
    energy = 40
    damage = 8
    resources = "Inf"
    description = "Vector's primary weapon would be powerful laser blasters attached to his flying pod. These blasters emit focused energy beams that can slice through obstacles and damage enemy vehicles."


class PlasmaGrenades(VectorWeapons):
    energy = 56
    damage = 13
    resources = 8
    description = "Vector could use plasma grenades that explode on impact, releasing fiery energy bursts that deal significant damage to enemy vehicles caught in the blast radius."


class SonicResonanceCannon(VectorWeapons):
    energy = 100
    damage = 22
    resources = 3
    description = "Fires powerful sonic waves that can shatter enemy shields and disrupt their systems, temporarily incapacitating them."


class GruShield:
    energy = None
    damage_reduction = None
    resources = None
    description = None

    def __str__(self):
        return self.__class__.__name__


class BarrierGun(GruShield):
    energy = 20
    damage_reduction = 0.4
    resources = "Inf"
    description = "The spaceship's shields create an invisible, energy-projected barrier around the vehicle. This barrier absorbs and dissipates energy- based attacks such as lasers, beams, and plasma shots."


class SelectivePermeability(GruShield):
    energy = 50
    damage_reduction = 0.9
    resources = 2
    description = "The shields can be programmed to allow certain objects, signals, or energies to pass through while blocking others. This can be useful for communication or specific tactical maneuvers."


class VectorShield:
    energy = None
    damage_reduction = None
    resources = None
    description = None

    def __str__(self):
        return self.__class__.__name__


class EnergyNetTrap(VectorShield):
    energy = 15
    damage_reduction = 0.32
    resources = "Inf"
    description = "Vector's pod might have the ability to deploy an energy net that ensnares enemy vehicles, temporarily immobilizing them and leaving them vulnerable to Vector's other attacks."


class QuantumDeflector(VectorShield):
    energy = 40
    damage_reduction = 0.8
    resources = 3
    description = "Manipulates quantum states to create a deflection field, causing enemy projectiles to miss the spaceship by a slight margin in the quantum realm."


def game_start():
    # Create villains
    gru = Gru("Gru")
    vector = Vector("Vector")
    i=0
    while gru.health>0 and vector.health>0:
        if i%2 ==0:
            # Gru's turn
            print('Its Gru turn choose a weapon for gru and a shield for vector')
            weapon = input('weapons:[FreezeGun, ElectricProd, MegaMagnet, KalmanMissile]:')
            shield = input('shields:[EnergyNetTrap, QuantumDeflector]:')

            gru.weapon = gru.choose_Weapon(weapon)
            vector.shield = vector.choose_Shield(shield)
            print(f"Gru used {weapon} against Vector!")
            gru.use_energy(gru.weapon.energy)
            vector.use_energy(vector.shield.energy)
            vector.apply_shield(vector.shield.damage_reduction)
            vector.take_damage(gru.weapon.damage)

        else:
            # Vector's turn
            print('Its Vector turn choose a weapon for vector and a shield for gru')
            weapon = input('weapons:[LaserBlasters, PlasmaGrenades, SonicResonanceCannon]:')
            shield = input('shields:[BarrierGun, SelectivePermeability]:')

            vector.weapon = vector.choose_Weapon(weapon)
            gru.shield = gru.choose_Shield(shield)
            print(f"Vector used {weapon} against Gru!")
            gru.use_energy(gru.shield.energy)
            vector.use_energy(vector.weapon.energy)
            gru.apply_shield(gru.shield.damage_reduction)
            gru.take_damage(vector.weapon.damage)

        # Print current state
        print(f"Gru's health: {gru.health}")
        print(f"Gru's energy: {gru.energy}")
        print(f"Vector's health: {vector.health}")
        print(f"Vector's energy: {vector.energy}")


game_start()