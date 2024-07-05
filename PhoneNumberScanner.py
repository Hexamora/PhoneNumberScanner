import phonenumbers
from phonenumbers import geocoder, carrier, timezone, NumberParseException
from geopy.geocoders import Nominatim

# Aksesoris
def print_banner():
    print("##########################################")
    print("#            Phone Number Scanner        #")
    print("#         Created by: Hexamora           #")
    print("##########################################")
    print()

def get_phone_number_info(phone_number_str):
    # Parse the phone number
    phone_number = phonenumbers.parse(phone_number_str)
    
    # Get the country and location
    country = geocoder.country_name_for_number(phone_number, "en")
    location = geocoder.description_for_number(phone_number, "en")
    
    # Get the timezone
    timezones = timezone.time_zones_for_number(phone_number)
    
    # Use geopy to get detailed location information
    geolocator = Nominatim(user_agent="phone_number_locator")
    geocode_location = geolocator.geocode(location, addressdetails=True)
    
    latitude = None
    longitude = None
    city = None
    region = None
    
    if geocode_location:
        latitude = geocode_location.latitude
        longitude = geocode_location.longitude
        address_details = geocode_location.raw.get('address', {})
        city = address_details.get('city', None)
        region = address_details.get('state', None)
    
    return {
        "country": country,
        "location": location,
        "timezones": timezones,
        "latitude": latitude,
        "longitude": longitude,
        "city": city,
        "region": region
    }

def scan_phone_number(phone_number_str):
    try:
        # Parsing nomor telepon
        parsed_number = phonenumbers.parse(phone_number_str, None)

        # Validasi nomor telepon
        is_valid = phonenumbers.is_valid_number(parsed_number)
        print(f"Nomor valid: {is_valid}")

        # Menampilkan nomor dalam format mentahnya
        print(f"Nomor yang di-parse: {parsed_number}")

        # Mendapatkan operator
        operator = carrier.name_for_number(parsed_number, "en")
        print(f"Operator: {operator}")

        # Format nomor telepon
        formatted_number_international = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_national = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        formatted_number_e164 = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        print(f"Format Internasional: {formatted_number_international}")
        print(f"Format Nasional: {formatted_number_national}")
        print(f"Format E164: {formatted_number_e164}")

        # Mendapatkan metadata
        country = geocoder.country_name_for_number(parsed_number, "en")
        metadata = phonenumbers.PhoneMetadata.metadata_for_region(country)
        if metadata:
            print(f"Panjang minimum nomor telepon untuk {country}: {metadata.general_desc.national_number_pattern.min_length}")
            print(f"Panjang maksimum nomor telepon untuk {country}: {metadata.general_desc.national_number_pattern.max_length}")

        # Mendapatkan informasi geolokasi
        info = get_phone_number_info(phone_number_str)
        print(f"Country: {info['country']}")
        print(f"Region: {info['region']}")
        print(f"City: {info['city']}")
        print(f"Latitude: {info['latitude']}")
        print(f"Longitude: {info['longitude']}")

    except NumberParseException as e:
        print(f"Error parsing number: {e}")

def main():
    print_banner()
    while True:
        phone_number_str = input("Masukkan nomor telepon yang ingin discan: ")
        scan_phone_number(phone_number_str)
        
        # Opsi untuk mengulang atau keluar
        choice = input("Apakah Anda ingin mengulang (yes/no)? ")
        if choice.lower() != 'yes':
            print("Terima kasih telah menggunakan Phone Number Scanner!")
            break

if __name__ == "__main__":
    main()
