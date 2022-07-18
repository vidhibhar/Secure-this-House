 # the build target executable:
TARGET = secure_house


all: $(TARGET)

$(TARGET): $(TARGET).py
	cp $(TARGET).py $(TARGET)
	chmod +x $(TARGET)

clean:
	$(RM) $(TARGET)