
#include <math.h>
#include <stdlib.h>

#define MYO_CHANNEL_SIZE 8
#define MYO_BUFFER_SIZE 50
#define MYO_SAMPLE_SIZE 25
#define MID_SAMPLE_INDEX 12

#define MODEL_NUM_LABEL 5



/* Pipeline Task
 *      Only runs when it receive an array of MYO_SAMPLE_SIZE (50) which equivalate to 250 ms of sampling
 *      
 *      Calculates Root Mean Square (RMS) value for each channel, which outputs a size 8 array, one for each channel. Then passes this vector through a standard scaler.
 *       To understand the numbers more information can found at ClubSynapsETS/Prothese
 *       Finaly, does a dot product with each label coeficient that were found using a support vector machine. If one is greater then 1 a pose has been identified.
 *
 *      Outputs trough a queue toward the main task the identified label.
 *
 *      NOTE: This task is heavy in processing time. It can delay the finger correction task.
 * */

void vPipeline_Pose( void * pvParam );
