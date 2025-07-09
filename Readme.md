
# 🏡 Lead Deal Prediction API

This API predicts key deal scores for property leads based on their preferences, financial details, and online behavior.

It returns:

* **faster\_closing\_score** → Likelihood that the deal will close quickly.
* **high\_return\_score** → Potential for high return (e.g., 2x–3x) on the deal.

---

## 📍 Endpoint

```
POST /predict
```

**URL:**
`http://34.71.143.146:8002/predict`

---

## 📄 Request Headers:

```http
Content-Type: application/json
```

---

## 📥 Sample Request Body (JSON):

```json
{
    "Property_Type_Interest": "Apartment",
    "Property_Purpose": "Investment",
    "Preferred_BHK": "4BHK",
    "Preferred_Furnishing": "Semi-furnished",
    "Parking_Needed": "Yes",
    "Preferred_Floor": "Top",
    "Ready_To_Move": "Yes",
    "Location_Preference": "HSR",
    "Occupation_Type": "Salaried",
    "Payment_Option": "Cash",
    "Job_Title_Public": "Manager",
    "Estimated_Income_Bracket_Public": "₹25L-₹50L",
    "PAN_Verified": "Yes",
    "GSTIN_Linked_Business": "No",
    "Property_Ownership_Records": "Yes",
    "Previous_Property_Transactions_Found": "No",
    "3rd_Party_Default_History_Flag": "No",
    "Fraud_Risk_Flag_3rd_Party": "No",
    "Family_Size": 4,
    "Budget": 90000000,
    "Website_Visits_Last_30_Days": 15,
    "Avg_Session_Duration_Minutes": 10,
    "Property_Page_Views": 25,
    "Saved_Property_Count": 2,
    "Virtual_Tour_Requests": 1,
    "Site_Search_Queries_Count": 4,
    "Contact_Agent_Clicks": 2,
    "WhatsApp_Inquiry_Responses": 1,
    "Lead_Form_Submissions": 1,
    "Email_Open_Rate": 70.0,
    "Email_Click_Through_Rate": 25.0,
    "Days_Since_Last_Visit": 5,
    "Frequency_of_Property_Shortlists": 3,
    "Call_Back_Request_Count": 1,
    "Time_Between_First_and_Last_Session_Days": 45,
    "Credit_Score_3rd_Party": 780,
    "Credit_Utilization_Percentage_3rd_Party": 20,
    "Loan_Eligibility_Score_3rd_Party": 0.85,
    "Distance_Metro_km": 2.5,
    "Distance_Hospital_km": 1.2,
    "Distance_Market_km": 1
}
```

---

## 🚀 Test API Using cURL:

```bash
curl --location 'http://34.71.143.146:8002/predict' \
--header 'Content-Type: application/json' \
--data '{ ... (same as above JSON) ... }'
```

---

## ✅ Example Response:

```json
{
    "faster_closing_score": 0.51,
    "high_return_score": 1.49
}
```

---

## 📝 Notes:

* **faster\_closing\_score:** A value between 0 and 1+ indicating faster deal closure likelihood (higher = better).
* **high\_return\_score:** Potential high return score; higher values mean better return potential.
* Make sure to send all fields in the request for correct prediction.

---

## 💡 Troubleshooting:

* If you get connection errors, ensure:

  * API server is running.
  * Correct IP/Port are used.
  * No firewall or proxy blocks the request.

---

Let me know if you also want Docker, Swagger, or Postman instructions!
