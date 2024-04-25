(define (problem ${instance_name})
  (:domain ${domain_name})

  ;Objects and their hierarchy 
  (:objects
    ${room_list}- room
    ${treasures_list}- treasure
    ${enemies_list}- enemy 
    ${weapons_list}- weapon
    ${potions_list}- potion 
  )

  ;Initial state's facts and numeric values
  (:init
    ;Hero initial position
    ${start_room}
    ;Dungeon exit room
    ${exit_room}
    ;Connected rooms (no door between them)
    ${room_links}
    ;Safe rooms (no enemies inside)
    ${safe_rooms} 
    ;Closed door between rooms (rooms are initially not connected)
    ${closed_doors}
    ;Keys position and counter
    ${keys_location}
    ${key_counter}
    ;Treasures position and value
    ${treasures_location}
    ${treasures_value}
    ;Enemies position and stats
    ${enemies_location} 
    ${enemies_life} 
    ${enemies_strength}
    ;Weapons position and strength
    ${weapons_location} 
    ${weapons_strength}
    ;Potions position and value
    ${potions_location} 
    ${potions_value} 
    ;Hero initial stats 
    ${hero_life}
    ${max_hero_life}
    ${hero_strength}
    ${hero_loot}
    ${defeated_enemy_counter}
  )

  ;Goal condition
  (:goal
    (and
      (escape) 
      ${loot_goal}
      ${life_goal}
      ${defeated_enemy_goal}
    )
  )
)