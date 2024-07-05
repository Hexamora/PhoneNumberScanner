# PhoneNumberScanner

The **"Phonenumberscanner"** script provided serves several primary purposes:

**Validation and Parsing of Phone Numbers:** This script utilizes the phonenumbers library to validate and parse user-inputted phone numbers, ensuring they adhere to expected formats.

**Phone Number Details:** The script retrieves information related to the phone number such as country, region, phone operator, international and national formats, and associated time zones.

**Geolocation:** Using the geopy library and Nominatim geolocation service, the script determines more precise geographic locations related to the phone number. Information such as latitude, longitude, and city can be obtained if available from the geolocation service.

**Iterative and Interactive:** Designed to operate iteratively and interactively, users are prompted to input the phone number they wish to scan. After retrieving information, users have the option to repeat the process or exit the program.

**Forensic or Investigative Use:** Such a script can be valuable in digital forensics or investigations to verify the validity of provided phone numbers, identify related geographic locations, and trace telecommunications service provider information.

Thus, **"Phonenumberscanner"** serves as a useful tool for checking and obtaining basic information regarding phone numbers, while adding a layer of geolocation for more detailed geographic information related to the phone number.

## Installation

Below is the sequence for installing scripts on Linux.

```bash
$ pip install phonenumbers geopy requests
$ git clone https://github.com/Hexamora/PhoneNumberScanner.git
$ cd PhoneNumberScanner
$ python PhoneNumberScanner.py
```
