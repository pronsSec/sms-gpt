# sms-gpt

# GPT Access via SMS Framework

This project provides a simple and streamlined framework for accessing GPT (Generative Pre-trained Transformer) models via SMS. It's designed to be easy to set up (taking about an hour) and is ideal for situations where traditional internet access is limited, such as in natural disasters, remote areas, or in countries where access to services like ChatGPT is restricted.

## Key Features

- **Simple Implementation**: A straightforward way to interact with GPT models via SMS.
- **Quick Setup**: Approximately one hour to get up and running.
- **Terraform Integration**: Streamlined deployment on Google Cloud Platform using Terraform.
- **Accessibility in Remote or Restricted Areas**: Reliable GPT access in situations with limited internet connectivity.

## Use Cases

- **Natural Disaster Response**: In areas affected by natural disasters where internet infrastructure is compromised.
- **Remote Area Connectivity**: For individuals in remote locations without stable internet access.
- **Circumventing Information Restrictions**: In regions where access to ChatGPT or similar AI services is blocked or restricted.

## Prerequisites

- Google Cloud account with billing set up.
- Terraform installed on your local machine.
- Basic knowledge of Google Cloud Platform and Terraform.

## Setup and Deployment

1. **Clone the Repository**: 
- git clone https://github.com/pronsSec/sms-gpt
2. **Configure Terraform**:
- Navigate to the Terraform configuration directory.
- Update the `main.tf` with your Google Cloud project details and credentials.
3. **Terraform Initialization and Apply**:
- terraform init
- terraform apply
- 4. **Configure Environment Variables**:
- Set up necessary environment variables for Twilio and OpenAI credentials in the startup script.

## Configuration

- Update the `startup-script.sh` with the necessary commands to install dependencies and run the Flask application.
- Modify the Flask application (`app.py`) as needed to suit your specific requirements.

## Usage

Once deployed, the framework allows users to send SMS messages to a specified Twilio number, which are then processed by the most recent GPT model, and the response is sent back via SMS.

## Contributing

Contributions to the project are welcome! Please refer to the contribution guidelines for more information.

## License

This project is licensed under Apache License 2.0. See the LICENSE file for more details.

## Disclaimer

This framework is intended for educational and research purposes and should be used responsibly, considering the ethical implications and respecting the laws and regulations of your respective country.

## Support and Contact

For support, feature requests, or any queries, please open an issue in the GitHub repository.

---

Enjoy accessing GPT models via SMS with this simple yet powerful framework!
