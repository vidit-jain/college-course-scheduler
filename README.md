# College Course Scheduler 
An initial development of a course scheduler usable by colleges. Uses OptaPlanner as the Constraint Satisfaction Engine

## Setup
To install all the necessary packages
```
pip install -r requirements.txt
```

Then, put the data in a `data/` in the root of the directory (Information about Rooms, Professors, Lessons & Timeslots). There is sample data already provided in the `data/` folder that corresponds to the IIIT 2024 Spring Semester. 

# Running Program
Once you've put the data in the folder, you can run the program

```
cd src
python main.py --timeslots timeslots.csv --rooms rooms.csv --lessons lessons.csv --teachers teachers.csv --seconds 60
```

The arguments provide the files that contain the concerned data, and the "seconds" parameter decides how long should the tool try to optimize the solution. Note that the tool assumes you put the file in the data folder, hence `timeslots.csv` is in the `data/` folder, not `src/`

Once you execute the program, you'll get an output file `final_timetable.txt` which is the solution provided by the tool.
