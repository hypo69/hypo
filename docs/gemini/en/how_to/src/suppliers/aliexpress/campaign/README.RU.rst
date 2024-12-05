rst
How to use the `campaign` module
========================================================================================

Description
-------------------------
The `campaign` module manages the creation and publishing of Facebook advertising campaigns. It includes functionality for initializing campaign parameters (name, language, currency), creating directory structures, saving campaign configurations, collecting and saving product data (using `ali` or `html` sources), generating advertising materials, validating the campaign, and publishing it to Facebook.  A flowchart illustrates the process.

Execution steps
-------------------------
1. **Initialization**:  The process begins by initializing the campaign's name, language, and currency.
2. **Directory Creation**:  Directories for the campaign and its categories are created.
3. **Configuration Saving**: The initialized campaign configuration is saved.
4. **Data Collection**: Product data is gathered, either through the `ali` data source or from `html` content.
5. **Data Storage**: Collected product data is saved for later use in the campaign.
6. **Material Generation**: Advertising materials are created based on the collected product data and campaign configuration.
7. **Validation**: The campaign is thoroughly validated to ensure all necessary components are present and correct.  This step likely involves checks for completeness and adherence to Facebook advertising guidelines.
8. **Campaign Readiness Check**: A check determines if the campaign is ready for publishing.  The loop returns to validation if the campaign is not ready.
9. **Publishing**: If the campaign is ready, it is published to Facebook.
10. **Completion**: The process concludes upon successful publishing.


Usage example
-------------------------
.. code-block:: python

    # Example initialization (replace with actual values)
    campaign_name = "Example Campaign"
    language = "en"
    currency = "USD"

    # ... (other necessary imports and configurations) ...

    from suppliers.aliexpress.campaign import create_campaign

    try:
        campaign_data = create_campaign(campaign_name, language, currency)
        # ... process the returned campaign data to handle product data ...

        # Example of checking for campaign readiness
        if campaign_data['ready_to_publish']:
            publish_result = create_campaign.publish_to_facebook(campaign_data)

            if publish_result:
                print("Campaign published successfully!")
            else:
                print("Failed to publish the campaign.")
        else:
            print("Campaign is not ready for publishing. Check for errors.")

    except Exception as e:
        print(f"An error occurred: {e}")