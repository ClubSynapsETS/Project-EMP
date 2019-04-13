/*#include "../bluetooth/ble_app.h"*/
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/queue.h"
#include "freertos/timers.h"

#include "../bluetooth/ble_app.h"
#include "../bluetooth/myohw.h"
#include "../Motion_control/finger_interface.h"
#include "../Pose_classification/pipeline.h"

#include <stdio.h>
#include <stdlib.h>
#include "driver/gpio.h"
#include "driver/adc.h"
#include "esp_adc_cal.h"
#include "esp_log.h"


#define TASK_FINGER_IFACE_PRIORITY  4
#define TASK_PIPELINE_PRIORITY      5

//Short cut simply to interface to with the finger interface because of unknow bug.
// creating a global shared structure for incoming instructions
volatile bt_shared_data_t bt_shared_buffer = {.myo_pose = 0, .data_read=1, 
                                              .finger_iface_task_name = "Finger_Interface",
                                              .finger_iface_handle = NULL,
                                              .tast_created=0}; 
volatile pipeline_shared_data_t share_pipeline = {.myo_pose = 0, .data_read=1, 
                                             .pipeline_task_name = "Pipeline",
                                             .finger_iface_handle = NULL,
                                             .tast_created=0}; 


void app_main(){

    int iteration =0;
    // lauching the BT client
    //connect to the other EMG raw attribute on the myo, we're ignoring the possible connection to a PC.
    bt_app_launch();

    
    //Start the finger interface
    xTaskCreate(vFingerInterface, bt_shared_buffer.finger_iface_task_name, 8056, &xQueue_to_pipeline, 
                    TASK_FINGER_IFACE_PRIORITY, NULL);

    //start pipeline and establish communcation with bleutooth
    xTaskCreate(vPipeline_Pose, share_pipeline.pipeline_task_name, 8056, &xQueue_to_pipeline,
                    TASK_PIPELINE_PRIORITY, NULL)
    

    for(;;){ 
        
        //if a bluetooth connection was not able to be established iterate between each pose.
        if( !bluetooth_connection ){

            if(iteration == 0)
                bt_shared_buffer.myo_pose = myohw_pose_fingers_spread;
            else if(iteration == 1)
                bt_shared_buffer.myo_pose = myohw_pose_fist;
            else if(iteration == 3)
                bt_shared_buffer.myo_pose = myohw_pose_wave_in;
            else if(iteration == 2)
                bt_shared_buffer.myo_pose = myohw_pose_wave_out;
            else if(iteration == 4)
                bt_shared_buffer.myo_pose = myohw_pose_wave_in;

            bt_shared_buffer.data_read = 0;
            iteration += 1;
            if(iteration>1) iteration =0;

            vTaskDelay(pdMS_TO_TICKS(3000));

        }

    }
}
