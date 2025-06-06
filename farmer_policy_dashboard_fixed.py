
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Farmer Policy Dashboard")

@st.cache_data
def load_data():
    return [
        {"cluster": 3, "name": "Stable Dairying Entrepreneurs", "tier": "Top", "rank": 1, "description": "Well-established dairy farmers with stable income and growth potential", "color": "#1f77b4",
         "policies": [{"name": "Premium Dairy Infrastructure Support", "scheme": "National Livestock Mission + AP Dairy Development", "budget": "₹5-10 lakhs", "priority": "High"},
                      {"name": "Dairy Export Facilitation", "scheme": "Agricultural Export Policy", "budget": "₹2-5 lakhs", "priority": "High"},
                      {"name": "Technology Adoption Incentives", "scheme": "AP Digital Agriculture Mission", "budget": "₹1-3 lakhs", "priority": "Medium"}]},
        {"cluster": 2, "name": "Dairying-Focused Commercial Farmers", "tier": "Top", "rank": 2, "description": "Commercial dairy farmers with expansion potential", "color": "#ff7f0e",
         "policies": [{"name": "Dairy Expansion Loans", "scheme": "NABARD + AP State Cooperative Banks", "budget": "₹3-8 lakhs", "priority": "High"},
                      {"name": "Feed and Fodder Security", "scheme": "AP Fodder Development Mission", "budget": "₹50,000-2 lakhs", "priority": "High"},
                      {"name": "Milk Marketing Support", "scheme": "AP Cooperative Dairy Development", "budget": "₹1-2 lakhs", "priority": "Medium"}]},
        {"cluster": 4, "name": "Mixed-Income Marginal Farmers", "tier": "Mid", "rank": 3, "description": "Farmers with diverse income sources but limited resources", "color": "#2ca02c",
         "policies": [{"name": "Integrated Farming System Support", "scheme": "MGNREGA + RKVY", "budget": "₹1-3 lakhs", "priority": "High"},
                      {"name": "Skill Development for Diversification", "scheme": "PMKVY", "budget": "₹25,000-75,000", "priority": "High"},
                      {"name": "Microfinance and SHG Support", "scheme": "AP Women's Cooperative Corporation", "budget": "₹50,000-1.5 lakhs", "priority": "Medium"}]},
        {"cluster": 6, "name": "Aspiring Diversified Farmers", "tier": "Mid", "rank": 4, "description": "Farmers seeking to diversify their agricultural activities", "color": "#d62728",
         "policies": [{"name": "Horticulture and Cash Crop Promotion", "scheme": "MIDH", "budget": "₹2-4 lakhs", "priority": "High"},
                      {"name": "Agri-entrepreneurship Development", "scheme": "AP Agri-Business Development", "budget": "₹1-3 lakhs", "priority": "Medium"},
                      {"name": "Market Linkage Support", "scheme": "e-NAM + FPO Development", "budget": "₹25,000-1 lakh", "priority": "Medium"}]},
        {"cluster": 1, "name": "Dairying-Only Subsistence Farmers", "tier": "Mid", "rank": 5, "description": "Small-scale dairy farmers focused on subsistence", "color": "#9467bd",
         "policies": [{"name": "Dairy Animal Enhancement", "scheme": "NLM + AP Livestock Development", "budget": "₹50,000-2 lakhs", "priority": "High"},
                      {"name": "Nutrition and Health Support", "scheme": "PM-KISAN", "budget": "₹6,000-12,000/year", "priority": "High"},
                      {"name": "Cooperative Membership Benefits", "scheme": "AP PACS", "budget": "₹10,000-50,000", "priority": "Medium"}]},
        {"cluster": 0, "name": "Diversified Low-Income Farmers", "tier": "Low", "rank": 6, "description": "Small farmers with multiple low-income activities", "color": "#8c564b",
         "policies": [{"name": "Livelihood Diversification Support", "scheme": "MGNREGA + DAY", "budget": "₹50,000-1.5 lakhs", "priority": "High"},
                      {"name": "Basic Infrastructure Development", "scheme": "AP Rural Infrastructure Mission", "budget": "₹25,000-1 lakh", "priority": "High"},
                      {"name": "Financial Inclusion Programs", "scheme": "Jan Dhan + KCC", "budget": "₹10,000-75,000", "priority": "Medium"}]},
        {"cluster": 5, "name": "Multi-Livestock Low-Income Farmers", "tier": "Low", "rank": 7, "description": "Farmers with multiple livestock but low income", "color": "#e377c2",
         "policies": [{"name": "Livestock Health and Nutrition", "scheme": "NADCP", "budget": "₹25,000-1 lakh", "priority": "High"},
                      {"name": "Livestock Insurance", "scheme": "PMFBY (Livestock)", "budget": "₹5,000-25,000", "priority": "High"},
                      {"name": "Value Addition Training", "scheme": "AP Skill Dev Corp", "budget": "₹15,000-50,000", "priority": "Medium"}]},
        {"cluster": 8, "name": "Potential But Currently Dormant", "tier": "Low", "rank": 8, "description": "Farmers with potential but currently inactive", "color": "#7f7f7f",
         "policies": [{"name": "Agricultural Revival Package", "scheme": "AP Farmer Revival Mission", "budget": "₹1-2 lakhs", "priority": "High"},
                      {"name": "Mentorship and Extension Services", "scheme": "KVK + ATMA", "budget": "₹10,000-50,000", "priority": "High"},
                      {"name": "Confidence Building Initiatives", "scheme": "AP Farmer Welfare", "budget": "₹5,000-25,000", "priority": "Medium"}]},
        {"cluster": 7, "name": "Inactive or Dormant Farmers", "tier": "Low", "rank": 9, "description": "Currently inactive farmers needing basic support", "color": "#bcbd22",
         "policies": [{"name": "Emergency Livelihood Support", "scheme": "MGNREGA + PM-KISAN", "budget": "₹20,000-75,000", "priority": "High"},
                      {"name": "Land Restoration Programs", "scheme": "AP Land Restoration Mission", "budget": "₹50,000-1.5 lakhs", "priority": "High"},
                      {"name": "Social Security Coverage", "scheme": "PM Kisan Maan Dhan Yojana", "budget": "₹1,000-5,000/year", "priority": "Medium"}]},
        {"cluster": 9, "name": "Extremely Low-Income Farmers", "tier": "Low", "rank": 10, "description": "Farmers in extreme poverty needing comprehensive support", "color": "#17becf",
         "policies": [{"name": "Comprehensive Welfare Package", "scheme": "AAY + IG Pension", "budget": "₹50,000-1 lakh/year", "priority": "High"},
                      {"name": "Rehabilitation and Skill Development", "scheme": "AP Rural Livelihood Mission", "budget": "₹25,000-75,000", "priority": "High"},
                      {"name": "Emergency Agricultural Support", "scheme": "PM-KISAN + Subsidies", "budget": "₹15,000-50,000", "priority": "Medium"}]}
    ]

cluster_data = load_data()

st.title("📊 Andhra Pradesh Farmer Cluster Policy Dashboard")
st.markdown("Interactive dashboard for analyzing 10 farmer clusters and associated policy recommendations.")

col1, col2, col3 = st.columns(3)
col1.metric("Total Clusters", len(cluster_data))
col2.metric("Policy Schemes", f"{sum(len(c['policies']) for c in cluster_data)}+")
col3.metric("Budget Range", "₹5K - 10L")

# Pie Chart
tier_df = pd.DataFrame([c['tier'] for c in cluster_data], columns=["Tier"])
tier_counts = tier_df["Tier"].value_counts().reset_index()
tier_counts.columns = ["Tier", "Count"]
pie = px.pie(tier_counts, names="Tier", values="Count", title="Cluster Distribution by Tier", hole=0.4)
st.plotly_chart(pie, use_container_width=True)

# Bar Chart
rank_df = pd.DataFrame([{"Cluster": f"{c['cluster']}: {c['name']}", "Rank": c["rank"], "Color": c["color"]} for c in cluster_data])
bar = px.bar(rank_df, x="Rank", y="Cluster", orientation="h", color="Cluster", title="Cluster Rankings",
             color_discrete_sequence=[c["color"] for c in cluster_data])
st.plotly_chart(bar, use_container_width=True)

# Cluster selection
cluster_options = {f"Cluster {c['cluster']}: {c['name']}": c for c in cluster_data}
selected_cluster_name = st.selectbox("Select Cluster for Detailed View:", ["All Clusters"] + list(cluster_options.keys()))

if selected_cluster_name != "All Clusters":
    c = cluster_options[selected_cluster_name]
    st.subheader(f"Cluster {c['cluster']}: {c['name']}")
    st.write(c["description"])
    st.markdown(f"**Tier**: {c['tier']} | **Rank**: {c['rank']}")
    st.markdown("### 🛠 Recommended Policies")
    for p in c["policies"]:
        st.markdown(f"- **{p['name']}** ({p['priority']} Priority): `{p['scheme']}` | Budget: {p['budget']}")
else:
    st.subheader("📋 All Cluster Summaries")
    for c in cluster_data:
        with st.expander(f"Cluster {c['cluster']}: {c['name']} ({c['tier']} Tier, Rank {c['rank']})"):
            st.write(c["description"])
            for p in c["policies"]:
                st.markdown(f"- **{p['name']}** ({p['priority']}): `{p['scheme']}` | Budget: {p['budget']}")

# Heatmap
st.markdown("### 🔥 Policy Intensity Heatmap")
heatmap_data = pd.DataFrame([
    {"Cluster": c["name"][:15] + "...",
     "Infrastructure": 9 if c["tier"] == "Top" else 6 if c["tier"] == "Mid" else 3,
     "Financial": 8 if c["tier"] == "Top" else 7 if c["tier"] == "Mid" else 9,
     "Technical": 9 if c["tier"] == "Top" else 5 if c["tier"] == "Mid" else 2,
     "Social": 3 if c["tier"] == "Top" else 5 if c["tier"] == "Mid" else 8}
    for c in cluster_data
])

fig = go.Figure(data=go.Heatmap(
    z=heatmap_data.drop(columns=["Cluster"]).values,
    x=heatmap_data.columns[1:],
    y=heatmap_data["Cluster"],
    colorscale='RdYlGn',
    reversescale=True,
    showscale=True
))
fig.update_layout(title="Policy Intensity Heatmap", xaxis_title="Policy Dimension", yaxis_title="Cluster")
st.plotly_chart(fig, use_container_width=True)
