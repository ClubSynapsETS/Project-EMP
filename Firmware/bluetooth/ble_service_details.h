
#include <stdint.h>


/* Service: Myo Mouvement
 *      Service UUID : 69a0977f-8fd5-434f-b506-0000658c1749
 *      Primary: is_primary
 *
 *   
 *   Characteristics //charact 128 bit uuid = Service_uuid | (CHRC_UUID << 32)
 *   {
 *      Mouvement
 *          UUID: 0x0001 
 *          flags: Notify
 *          Description: Server will output upon processing raw Myo data the desired mouvememnt
 *                       for the prosthesis. It will notify the client that a new mouvement is
 *                       required.
 *
 *      Mode
 *          UUID: 0x0002
 *          flags: Read
 *
 *          Description: It Will contain the desired mode for the prosthesis. Currently three 
 *          modes are defined: Myo_dirconnect, a direct connection to the myo.
 *                             Demo_mode, Alternate between pre-programe mouvements.
 *                             Human_crtl_mode, subscribe to MouvementChrc.
 *
 *      Logs
 *          UUID: 0x0003
 *          flags: Write
 *
 *          Description: Send information important to the main application, such as current 
 *                       battery level or how errors were handled.
 *   }
 */

// defining interface PC UUIDs
#define ZACKB_BDA   { \
    0x00, 0x1A, 0x7D, \
    0xDA, 0x71, 0x13  \
}
#define DAVID_BDA   { \
    0x30, 0x3A, 0x64, \
    0x5E, 0x86, 0xD3  \
}

#define MYO_ARMBAND_BDA   { \
    0xD0, 0x59, 0x3D, \
    0x4E, 0xe8, 0x31  \
}


// defining service UUIDs
#define MYO_MOUVEMENT_SERVICE_UUID { \
    0x49, 0x17, 0x8c, 0x65,          \
    0x00, 0x00, 0x06, 0xb5,          \
    0x4f, 0x43, 0xd5, 0x8f,          \
    0x7f, 0x97, 0xa0, 0x69           \
}
#define MYOMV_POSE_CHRC_UUID       { \
    0x49, 0x17, 0x8c, 0x65,          \
    0x01, 0x00, 0x06, 0xb5,          \
    0x4f, 0x43, 0xd5, 0x8f,          \
    0x7f, 0x97, 0xa0, 0x69           \
}


#define MYO_SERVICE_EMG0_UUID { \
    0x42, 0x48, 0x12, 0x4a,     \
    0x7f, 0x2c, 0x48, 0x47,     \
    0xb9, 0xde, 0x04, 0xa9,     \
    0x05, 0x01, 0x06, 0xd5      \
}
#define MYO_SERVICE_EMG1_UUID { \
    0x42, 0x48, 0x12, 0x4a,     \
    0x7f, 0x2c, 0x48, 0x47,     \
    0xb9, 0xde, 0x04, 0xa9,     \
    0x05, 0x02, 0x06, 0xd5      \
}
#define MYO_SERVICE_EMG2_UUID { \
    0x42, 0x48, 0x12, 0x4a,     \
    0x7f, 0x2c, 0x48, 0x47,     \
    0xb9, 0xde, 0x04, 0xa9,     \
    0x05, 0x03, 0x06, 0xd5      \
}
#define MYO_SERVICE_EMG3_UUID { \
    0x42, 0x48, 0x12, 0x4a,     \
    0x7f, 0x2c, 0x48, 0x47,     \
    0xb9, 0xde, 0x04, 0xa9,     \
    0x05, 0x04, 0x06, 0xd5      \
}
