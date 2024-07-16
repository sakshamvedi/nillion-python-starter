from nada import Nada, Signature, UInt64, Int64, Array, String

class FraudDetection(Nada):
    transaction_amount = UInt64()
    merchant_category = String(100)  
    transaction_time = UInt64()
    user_location = String(100)

    def compute(self):
        risk_score = 0
        
        
        if self.transaction_amount > 1000:
            risk_score += 5
        
        if self.merchant_category == "Luxury Goods" and self.user_location == "Small Town":
            risk_score += 8
            
        
        if self.transaction_time % 86400 < 3600 or self.transaction_time % 86400 > 82800: 
            risk_score += 3
            
      
        is_fraudulent = risk_score > 10  
        return {'is_fraudulent': is_fraudulent, 'risk_score': risk_score}


fraud_detection_signature = Signature(FraudDetection)