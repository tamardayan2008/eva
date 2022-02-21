def P_gyro (drivebase, gyro, speed, target, kp, distance):
    while (drivebase.distance() < distance):
        drivebase.drive (speed, (gyro.angle() - target) * kp)