deps_config := \
	/home/zackb/Synapse/esp32/esp-idf/components/app_trace/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/aws_iot/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/bt/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/driver/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/esp32/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/esp_adc_cal/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/esp_http_client/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/ethernet/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/fatfs/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/freertos/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/heap/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/http_server/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/libsodium/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/log/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/lwip/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/mbedtls/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/mdns/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/mqtt/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/nvs_flash/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/openssl/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/pthread/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/spi_flash/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/spiffs/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/tcpip_adapter/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/vfs/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/wear_levelling/Kconfig \
	/home/zackb/Synapse/esp32/esp-idf/components/bootloader/Kconfig.projbuild \
	/home/zackb/Synapse/esp32/esp-idf/components/esptool_py/Kconfig.projbuild \
	/home/zackb/Synapse/esp32/esp-idf/components/partition_table/Kconfig.projbuild \
	/home/zackb/Synapse/esp32/esp-idf/Kconfig

include/config/auto.conf: \
	$(deps_config)

ifneq "$(IDF_CMAKE)" "n"
include/config/auto.conf: FORCE
endif

$(deps_config): ;
