; DUNGEON RESOLVER
; Pddl domain that define a dungeon's structure, where a hero try to escape exploring rooms, collecting loot and defeating enemies... staying alive.

(define (domain dungeon)

;General requirements
(:requirements :strips :fluents :durative-actions :timed-initial-literals :typing :conditional-effects :negative-preconditions :duration-inequalities :equality)

;Types and their hierarchy 
(:types 
    ;Rooms that compose dungeon
    room 
    ;Loot that hero can find in rooms
    treasure
    ;Enemies that populate rooms
    enemy
    ;Weapon that hero can find in rooms to defeat enemies
    weapon
    ;Potion that hero can find in rooms to healt
    potion
)

;(:constants )

;Predicates
(:predicates 
    ;Position inside dungeon 
    (at ?x - room)
    ;Connection between rooms 
    (connected ?x ?y - room)
    ;Exit room to reach 
    (exit_room ?x - room)
    ;Escape from dungeon
    (escape)
    ;Closed doors with key between rooms 
    (closed_door ?x ?y - room)
    ;Key position
    (key_at ?x - room)
    ;Treasures position
    (treasure_at ?t - treasure ?x - room)
    ;Enemies position
    (enemy_at ?e - enemy ?x - room)
    ;Rooms safe, without enemies 
    (room_safe ?x - room)
    ;Weapon position
    (weapon_at ?w - weapon ?x - room)
    ;Potions position
    (potion_at ?p - potion ?x - room)
    ;Potions own
    (own_potion ?p - potion)   
)

(:functions
    ;Hero stats
    (hero_life)
    (max_hero_life)
    (hero_strength)
    (hero_loot)
    (defeated_enemy_counter)
    ;Number of keys owned
    (key_counter)
    ;Treasures value
    (treasure_value ?t - treasure)
    ;Enemies stats
    (enemy_life ?e - enemy)
    (enemy_strength ?e - enemy)
    ;Weapons strength
    (weapon_strength ?w - weapon)
    ;Potions value
    (potion_value ?p - potion)
)
   
;Actions

;Move between rooms if they are connected (possible door between rooms open) and starting room safe (no enemies inside)
(:action move
    :parameters (?x ?y - room)
    :precondition (and (at ?x) (connected ?x ?y))
    :effect (and (at ?y) (not (at ?x)))
)

;Escape from dungeon if exit_room reached
(:action escape_from_dungeon
    :parameters (?x - room)
    :precondition (and (at ?x) (exit_room ?x))
    :effect (and (not (at ?x)) (escape))
)

;Collect key from safe room (no enemies inside): key_counter increased by 1
(:action collect_key
    :parameters (?x - room)
    :precondition (and (at ?x) (key_at ?x))
    :effect (and (not (key_at ?x)) (increase (key_counter) 1))
)

;Open door between 2 rooms using key (two rooms with door between them are initially not connected): key_counter decreased by 1
(:action open_door
    :parameters (?x ?y - room)
    :precondition (and (at ?x) (closed_door ?x ?y) (>= (key_counter) 1))
    :effect (and (not (closed_door ?x ?y)) (connected ?x ?y) (connected ?y ?x) (decrease (key_counter) 1))
)

;Collect treasures from room: hero_loot increased by treasure_value
(:action collect_treasure
    :parameters (?t - treasure ?x - room)
    :precondition (and (at ?x) (treasure_at ?t ?x))
    :effect (and (not (treasure_at ?t ?x)) (increase (hero_loot) (treasure_value ?t)))
)

;Defeat enemies in the room if hero_strength >= enemy_life; hero_life decreased by enemy_strength, defeated_enemy_counter increased by 1
(:action defeat_enemy
    :parameters (?e - enemy ?x - room)
    :precondition (and (at ?x) (enemy_at ?e ?x) (> (hero_life) (enemy_strength ?e)) (>= (hero_strength) (enemy_life ?e)))
    :effect (and (not (enemy_at ?e ?x)) (room_safe ?x) (decrease (hero_life) (enemy_strength ?e)) (increase (defeated_enemy_counter) 1))
)

;Collect potions from safe room (no enemies inside)
(:action collect_potion
    :parameters (?p - potion ?x - room)
    :precondition (and (at ?x) (potion_at ?p ?x) (room_safe ?x))
    :effect (and (not (potion_at ?p ?x)) (own_potion ?p))
)

;Drink potions if hero_life <= max_hero_life - potion_value; hero_life increased by potion_value
(:action drink_potion
    :parameters (?p - potion)
    :precondition (and (own_potion ?p) (<= (hero_life) (- (max_hero_life) (potion_value ?p))) (not (escape)))
    :effect (and (not (own_potion ?p)) (increase (hero_life) (potion_value ?p)))
)

;Collect weapon: assign weapon_value at hero_stregth
(:action collect_weapon
    :parameters (?w - weapon ?x - room)
    :precondition (and (at ?x) (weapon_at ?w ?x))
    :effect (and (not (weapon_at ?w ?x)) (assign (hero_strength) (weapon_strength ?w)))
)

)