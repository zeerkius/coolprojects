package BasilAgboola;

import java.lang.Math;

import robocode.HitByBulletEvent;
// I eneded up not needing math
import robocode.HitRobotEvent;
import robocode.HitWallEvent;
import robocode.Robot;
import robocode.ScannedRobotEvent;
// I Imported all of these because on looking at thenthe other robots source code they all had this
// So im doing this to make sure it runs becuase its impossible for me to run it on the thing
//class Slayer{

    //package robotslayeralgo;
    //import robocode.*;
   
//   double degrees = 0;
//   double distance = 0;


    //import java.awt.Color;
    
    // API help : https://robocode.sourceforge.io/docs/robocode/robocode/Robot.html
    
    /**
     * RobotSlayer - a robot by (Basil Agboola)
     */
   
public class Slayer extends Robot
    {
        /**
         * run: RobotSlayer's default behavior
         */
        public void run() {
            // Initialization of the robot should be put here
    
            // After trying out your robot, try uncommenting the import at the top,
            // and the next line:
    
            // setColors(Color.red,Color.blue,Color.green); // body,gun,radar
    
            // Robot main loop
            while(true) {
                // Replace the next 4 lines with any behavior you would like
                //ahead(100);
                //turnGun(180);
                //turnGunLeft(180);
            }

            
        }
    
        /**
         * onScannedRobot: What to do when you see another robot
         */
        public void onScannedRobot(ScannedRobotEvent e) {
            // Replace the next line with any behavior you would like
 
                double degrees = e.getBearing();
                turnGunLeft(degrees - 90);
                fire(1);
                // Will now scann robot and turn exactly the amount of degress it is from the robot and fire
            
            
            
            
            
        }
    
        /**
         * onHitByBullet: What to do when you're hit by a bullet
         */
        public void onHitByBullet(HitByBulletEvent e) {
            // Replace the next line with any behavior you would like
            back(10);
            getEnergy();
            fire(5);
            // gets energy to keep it alive
        }
        
        /**
         * onHitWall: What to do when you hit a wall
         */
        public void onHitWall(HitWallEvent e) {
            // Replace the next line with any behavior you would like
            back(50);
            
            getEnergy();
            fire(5);
            //Get eneergy back in case its cornered 
        }	
    }
//}