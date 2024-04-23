(define (problem ${instance_name})
  (:domain ${domain_name})

  ;Objects and their hierarchy 
  (:objects
    ${room_list} - room
    ${treasures_list} - treasure
    ${enemies_list} - enemy 
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
    ;Treasure position and value
    ${treasures_location}
    ${treasures_value}
    ;Enemy position and stats
    ${enemies_location} 
    ${enemies_life} 
    ${enemies_strength} 
    ;Hero initial stats
    ${hero_loot}
  )

  ;Goal condition
  (:goal
    (and
      (escape) (>= (hero_loot) ${loot_goal})
    )
  )
)