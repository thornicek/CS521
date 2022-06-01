package CS526_Hw;

import java.io.IOException;
import java.io.File;
import java.util.Scanner;
public class Hw1_p2 {

    public static void findByMake(Car[] cars, String make) {
        // implement this method
    	boolean checkMake = false;
    	for(int i = 0;i< cars.length;i++) {
    		if(cars[i].getMake().equals(make)) {
    			System.out.println(cars[i]);
    			checkMake = true;
    		}
    			
    	}
    	if(!checkMake) {
    		System.out.println("No car with that make exists");
    	}

    }

    public static void olderThan(Car[] cars, int year) {
        // implement this method
    	boolean checkYear = false;
    	for(int i = 0; i < cars.length; i++) {
    		if(cars[i].getYear() < year) {
    			System.out.println(cars[i]);
    			checkYear = true;
    		}
    	}
    	if(!checkYear) {
    		System.out.println("No car older than the year is contained in the array");
    	}
    }

    public static void main(String[] args) throws IOException {

        // complete this part
        // create an array of Car objects, cars, of size 10
        // read input file and store 10 car Objects in the array
    	System.out.println(new File(".").getAbsolutePath());
        Car[] cars = new Car[10];
        File myObj = new File("/Users/tomas/Desktop/JavaProjects/CS526_HW1/src/CS526_Hw/car_input.txt");
        Scanner myReader = new Scanner(myObj);
        int counter = 0;
        while (myReader.hasNextLine()) {
        	String line = myReader.nextLine();
            String[] data = line.split(",");
            String make = data[0];
            String priceString = data[1];
            priceString = priceString.trim();
            String yearString = data[2];
            yearString = yearString.trim();
            int yearInt = Integer.parseInt(yearString);
            int priceInt = Integer.parseInt(priceString);
            Car car = new Car(make, yearInt, priceInt);
            cars[counter] = car;
            counter++;

        }


        System.out.println("\nAll cars:");
        for (int i=0; i<cars.length; i++) {
            System.out.println(cars[i]);
        }

        String make = "Honda";
        int year = 2017;

        System.out.println("\nAll cars made by " + make);
        findByMake(cars, make);
        System.out.println("\nAll cars made before " + year);
        olderThan(cars, year);
    }

}


