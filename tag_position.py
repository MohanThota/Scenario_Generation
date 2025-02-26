import carla

def main():
    # Connect to the CARLA server
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)  # Set a timeout for the connection

    # Get the world object
    world = client.load_world('Town01') 

    # Retrieve all spawn points from the map
    spawn_points = world.get_map().get_spawn_points()

    # Print each spawn point with its index, location, and rotation
    print("Available Spawn Points:")
    for idx, spawn_point in enumerate(spawn_points):
        location = spawn_point.location
        rotation = spawn_point.rotation
        print(f"Spawn Point {idx}: Location(x={location.x:.2f}, y={location.y:.2f}, z={location.z:.2f}), "
              f"Rotation(pitch={rotation.pitch:.2f}, yaw={rotation.yaw:.2f}, roll={rotation.roll:.2f})"
             # Make the spawn point glow by drawing a marker
        world.debug.draw_string(
            location,
            f"Spawn Point {idx}",
            draw_shadow=False,
            color=carla.Color(255, 0, 0),  # Red color
            life_time=1000.0,  # Marker will persist for 10 seconds
            persistent_lines=True
        )


if __name__ == "__main__":
    main()

