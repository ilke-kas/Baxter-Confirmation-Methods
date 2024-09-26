# Human-Robot Interaction: Confirmation Methods for Deictic Gestures

## Abstract
This study investigates different confirmation methods employed by the Baxter robot for deictic gestures in Human-Robot Interaction (HRI). Motivated by the need to enhance user experience, we explore the impact of various confirmation modalities on the retrieval of a pointed object.

## Introduction
In Human-Computer Interaction, certain scenarios necessitate confirming computer actions. For instance, using Homepod to instruct Siri to control a humidifier may lack feedback, leading to potential misinterpretations. To enhance user experience, we explore if incorporating diverse confirmation methods can mitigate variability and improve user interaction. This study investigates the impact of robot confirmation methods on user experience while the Baxter robot retrieves a designated object. 

We designed an experiment and analyzed the data to learn how different confirmation methods in HRI with gestures impact the user experience in terms of likability, animacy, etc. We proved that different kinds of confirmation methods play an important role in HRI, and we also found out which kind of confirmation method that participants have the best user experience with.

## Previous Research
Most of the existing studies focus on improving the technical aspects of dynamic hand gesture recognition, hand pose estimation, eye tracking, and object recognition, along with task completion accuracy to enhance HRI. One previous study involving deictic gestures in a Pick-and-Place task showed that any kind of confirmation gestures and methods improves task completion accuracy and efficiency, as well as user experience. However, this study only utilized a visual confirmation method by showing the image of the object to the participants.

There are other studies that focus on the communication aspects of HRI. These studies have examined the impact of visual, auditory, tactile, and other non-verbal cues to improve human-robot communication. However, they lack experimental results regarding the differences in user experience.

## Proposed Study
The proposed study explores which robot confirmation methods are preferred by users. The main goal of this exploration is to improve user experience by analyzing likability, anthropomorphism, animacy, perceived intelligence, and safety of the different confirmation methods. For this purpose, we used four different methods:

- **Visual Confirmation Method**: The image of the pointed object is shown to the participant on the screen of the robot.
- **Verbal Confirmation Method**: The robot verbally asks participants the color of the object.
- **Body Movement Confirmation Method**: The robot uses its arm to confirm the pointed object by moving its arm towards the pointed object and opening and closing its gripper.
- **No Confirmation Method (Baseline Method)**: The robot does not use any confirmation method.

### Experimental Question
We investigate the following exploratory experimental question: “How do the different confirmation methods of the robot (visual, verbal, body movement, or no confirmation) affect the user experience during the retrieval of the pointed object?”. We expect to find a significant difference in user experience when the robot employs different confirmation methods during the retrieval of a pointed object using a deictic hand gesture (Hypothesis 1).

## Methods
During the experiment, we deceived participants by stating that the robot could detect their deictic hand gestures to perceive the pointed object. However, we controlled the robot using the Robot Operating System (ROS) terminal by running previously decided commands. We located the experimenter in front of the computer in a way that they could see the pointed object by the participant, allowing them to run the corresponding command based on the pointed object.

### Visual Confirmation Method
For the visual confirmation method, we displayed three different colored cube (red, blue, and green) images on the screen of the robot by running the corresponding ROS command.

### Verbal Confirmation Method
For the verbal confirmation method, we placed an unseen JBL speaker behind the robot. We connected one of the experimenters’ phones to the JBL speaker to play three different audio clips for three different colored cubes according to the color of the pointed object.

### Body Movement Confirmation Method and Handing Over the Object
For the body movement confirmation method and handing over the object, we first fixed the positions of the cubes on the table. After that, we saved three different arm routines by controlling the arm from our keyboard. Every time a participant points to one of the cubes, we replayed the corresponding arm routine for that cube.

## Conclusion
The findings from this study aim to improve Human-Robot Interaction by identifying effective confirmation methods that enhance user experience during the retrieval of objects by robots.
