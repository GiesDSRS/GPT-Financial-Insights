# GPT-Financial-Insights

`GPT-Financial-Insights` is an open-source tool that leverages the GPT (Generative Pre-trained Transformer) models provided by OpenAI to analyze and extract insights from financial documents. Built with Streamlit, this tool offers an interactive web interface that allows users to input financial texts and receive detailed AI-generated analyses.

## Features

- Interactive Streamlit interface for easy use.
- Ability to process large financial documents in manageable chunks.
- Utilizes OpenAI's advanced GPT models for accurate text analysis.
- Designed to maintain context across document sections for coherent analysis.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following installed:
- Python 3.6 or higher
- Streamlit
- OpenAI Python library

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/pratikrelekar/GPT-Financial-Insights.git
cd GPT-Financial-Insights
```
### Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Usage
Run the Streamlit application:
```bash
streamlit run app.py
```
Follow the on-screen prompts to input the path to your financial document and your query.

### Configuration
You will need to set your OpenAI API key as an environment variable. For security reasons, integrate this key in your application.
```bash
export OPENAI_API_KEY='your-api-key'
```
## License and Disclaimer

### License

`GPT-Financial-Insights` is made available under the MIT License. This license permits reuse within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.

You can view the full MIT License in the [LICENSE](https://opensource.org/license/afl-3-0-php/) file accompanying this source code.

### Disclaimer

While `GPT-Financial-Insights` is open-source and freely available, users should be aware that the application relies on the OpenAI API, which has its own set of terms and conditions. Users are responsible for adhering to OpenAI's [terms of service](https://openai.com/terms/) when using this application.

Furthermore, the financial analysis capabilities of this tool are dependent on the information processed through the OpenAI API. `GPT-Financial-Insights` does not generate or infer financial data on its own. Instead, it relies on the GPT model's ability to interpret and analyze text based on pre-existing knowledge up to a certain date (as per OpenAI's data cut-off for model training). The tool is not a substitute for professional financial advice or analysis. It should not be used as the sole basis for any financial decision-making.

As the developer of `GPT-Financial-Insights`, I do not claim responsibility for any decisions made based on the analyses provided by this tool. Users should employ their judgment and/or consult with qualified financial advisors before making financial decisions.


Contact

Author: Pratik Relekar, Qingwen (Freya) Liang, Matias Carrasco Kind
Email: pratik.relekar@gmail.com
Project Link: GPT-Financial-Insights


