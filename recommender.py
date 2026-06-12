# recommender.py
"""
Content-Based Recommendation Engine using Machine Learning (TF-IDF + Cosine Similarity).
Recommends destinations similar to the one selected by the user.
"""

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

def get_recommendations(selected_city, destinations_dict, top_n=3):
    """
    Computes content-based similarity between the selected city and other cities.
    Returns a list of tuples: (city_name, similarity_score_percentage, matching_reason)
    """
    if not destinations_dict or selected_city not in destinations_dict:
        return []

    cities = list(destinations_dict.keys())
    
    if len(cities) <= 1:
        return []

    if SKLEARN_AVAILABLE:
        # Build features text for TF-IDF Vectorization
        features = []
        for city in cities:
            data = destinations_dict[city]
            # Combine category, region, state, and description into a single text document
            text = f"{data['category']} {data['region']} {data['state']} {data['description']}"
            features.append(text)

        # Fit TF-IDF Vectorizer
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(features)

        # Compute Cosine Similarity matrix
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # Get index of the selected city
        idx = cities.index(selected_city)

        # Get similarity scores for all cities with the selected city
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the cities based on similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Filter out the selected city itself and get top_n recommendations
        recommendations = []
        for i, score in sim_scores:
            city_name = cities[i]
            if city_name == selected_city:
                continue
            
            # Format score as percentage
            score_pct = int(score * 100)
            
            # Generate a dynamic reason based on matching category/region/state
            reasons = []
            selected_data = destinations_dict[selected_city]
            rec_data = destinations_dict[city_name]
            
            if selected_data["category"] == rec_data["category"]:
                reasons.append(f"same style ({selected_data['category']})")
            if selected_data["region"] == rec_data["region"]:
                reasons.append(f"same region ({selected_data['region']} India)")
            if selected_data["state"] == rec_data["state"]:
                reasons.append(f"same state ({selected_data['state']})")
                
            reason_str = ", ".join(reasons) if reasons else "similar atmosphere & travel attributes"
            
            recommendations.append((city_name, score_pct, reason_str))
            
            if len(recommendations) >= top_n:
                break
                
        return recommendations
    else:
        # Fallback heuristic similarity if scikit-learn is not installed
        selected_data = destinations_dict[selected_city]
        scores = []
        
        for city_name in cities:
            if city_name == selected_city:
                continue
                
            rec_data = destinations_dict[city_name]
            score = 0.0
            reasons = []
            
            if selected_data["category"] == rec_data["category"]:
                score += 0.4
                reasons.append(f"same style ({selected_data['category']})")
            if selected_data["region"] == rec_data["region"]:
                score += 0.3
                reasons.append(f"same region ({selected_data['region']} India)")
            if selected_data["state"] == rec_data["state"]:
                score += 0.2
                reasons.append(f"same state ({selected_data['state']})")
                
            # Basic overlap in description
            desc1_words = set(selected_data["description"].lower().split())
            desc2_words = set(rec_data["description"].lower().split())
            overlap = len(desc1_words.intersection(desc2_words)) / max(len(desc1_words), 1)
            score += min(overlap * 0.5, 0.1)
            
            score_pct = int(score * 100)
            reason_str = ", ".join(reasons) if reasons else "similar atmosphere & travel attributes"
            
            scores.append((city_name, score_pct, reason_str))
            
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        return scores[:top_n]
