(define (domain simple_dungeon)

;General requirements
(:requirements :strips :fluents :durative-actions :timed-initial-literals :typing :conditional-effects :negative-preconditions :duration-inequalities :equality)

;Types and their hierarchy 
(:types 
    ;Rooms that compose dungeon
    room 
    ;Loot that hero can find in rooms
    treasure
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
)

(:functions
    ;Number of keys owned
    (key_counter)
    ;Treasures value
    (treasure_value ?t - treasure)
    ;Hero stats
    (hero_loot)
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

;Collect key from safe room (no enemies inside)
(:action collect_key
    :parameters (?x - room)
    :precondition (and (at ?x) (key_at ?x))
    :effect (and (not (key_at ?x)) (increase (key_counter) 1))
)

;Open door between 2 rooms using key (two rooms with door between them are initially not connected)
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

)