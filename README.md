# GmapZ

GmapZ is a Python-based application designed to fetch business information from Google Maps. It uses the Google Maps API to retrieve details like business names, phone numbers, addresses, website URLs, and review counts. The data is presented in a simple GUI and can be exported to an Excel file. This tool is especially useful for businesses looking to identify potential clients who may require website development services.

## Features

- Fetch business information from Google Maps based on user-defined keywords and location.
- Extract details such as Name, Phone Number, Address, Website URL, and Reviews Count.
- GUI for easy interaction and real-time progress tracking.
- Export the fetched data to an Excel file.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed.
- Google Maps API key (You can obtain one from [Google Cloud Platform](https://cloud.google.com/maps-platform)).

## Installation

To install GmapZ, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/GmapZ.git
````
2. Navigate to the cloned directory:

cd GmapZ

3. Install required Python packages:

```bash
pip install googlemaps pandas
````

## Usage

To use GmapZ, follow these steps:

1. Run the main script:

```bash
python gmapz.py
````
2. Enter the location coordinates (latitude,longitude) and the search keyword in the provided text fields.
3. Click on 'Fetch Data' to start the process.
4. Once the data fetching is complete, the results will be saved in an `output.xlsx` file in the same directory.

## Contributing to GmapZ

To contribute to GmapZ, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contributors

Thanks to the following people who have contributed to this project:

- [@ravitejachillara](https://github.com/ravitejachillara)

## Contact

If you want to contact me, you can reach me at `iamravitejachillara@gmail.com`.

## License

This project uses the following license: [MIT License](https://github.com/ravitejachillara/GmapZ/blob/main/LICENSE)


