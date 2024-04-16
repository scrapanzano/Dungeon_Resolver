(define (problem ${instance_name})
  (:domain ${domain_name})
  (:objects
    ${room_list} - room
    ${treasures_list} - treasure
  )
  (:init
    ${start_room}
    ${exit_room}
    ${room_links}
    ${closed_doors}
    ${keys_location}
    ${key_counter}
    ${treasures_location}
    ${treasures_value}
    ${hero_loot}
  )

  (:goal
    (and
      (escape) ( >= (hero_loot) 50)
    )
  )
)