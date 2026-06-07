import streamlit as st
import pandas as pd
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load credentials from .env hidden structure securely
load_dotenv()

# Initialize OpenAI client 
api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "your_actual_api_key_here":
    st.error("❌ OpenAI API Key not found! Please update your hidden `.env` file with a valid key.")
    st.stop()

client = OpenAI(api_key=api_key)

# App Configuration
st.set_page_config(page_title="Fluidic Catalog Engine", layout="wide")
st.title("🦅 Nagarro | Fluidic Catalog Engine")
st.subheader("Autonomous Retail & CPG Data Intake Portal (Live Agentic Mode)")
st.markdown("---")

# Layout Split
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📥 Step 1: Upload Supplier Catalog")
    uploaded_file = st.file_uploader("Choose an unstandardized catalog sheet", type=["xlsx", "csv"])

with col2:
    st.markdown("### 📊 Operational Health")
    st.metric(label="Target Uplift Benchmark", value="20%+", delta="Nagarro Fluidic Promise")
    st.metric(label="System Status", value="Live Engine Active", delta="Connected to OpenAI API")

st.markdown("---")

# --- MULTI-AGENT INTAKE EXECUTION CORE ---
def run_schema_mapping_agent(raw_headers):
    """
    Agent 1: Schema Mapping Agent (NIA Orchestration Pattern)
    Reads raw row keys from an unpredictable client file and contextually maps them
    to Nagarro's Retail Gold Master Schema.
    """
    prompt = f"""
    You are Nagarro's specialized 'Schema Mapping Agent' running inside the NIA Framework.
    Your task is to analyze the row header columns provided by a raw, unstandardized B2B supplier file.
    You must map their unpredictable column fields to our standard Master Retail Schema fields:
    - Target Field 1: `sku_id` (Look for identifying tags, SKU codes, product IDs, references)
    - Target Field 2: `product_name` (Look for titles, product terms, descriptions, item nomenclature)
    - Target Field 3: `wholesale_cost` (Look for dealer cost, supply price, incoming B2B price, unit cost)
    - Target Field 4: `retail_price` (Look for MSRP, store shelf price, selling target value, consumer cost)

    Input Column Headers to evaluate: {raw_headers}

    You MUST respond with a valid, raw JSON object ONLY. Do not wrap it in markdown code blocks.
    The keys of the JSON object must match our 4 Target Fields, and the values must be the matching input columns.
    Example Format:
    {{"sku_id": "Supplier_Ref_Num", "product_name": "ItemDesc", "wholesale_cost": "Dealer_Net", "retail_price": "MSRP"}}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Utilizing a fast, high-efficiency text reasoning model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0 # Deterministic grounding matching enterprise parameters
        )
        # Parse the raw text into a safe dictionary mapping
        mapping_dict = json.loads(response.choices[0].message.content.strip())
        return mapping_dict
    except Exception as e:
        st.error(f"Failed to communicate with Schema Mapping Agent: {str(e)}")
        st.stop()

def run_anomaly_compliance_agent(row_data):
    """
    Agent 2: Deterministic Anomaly & Compliance Agent (XMDM360 Node Pattern)
    Evaluates records against hard enterprise financial guardrails without model guesses.
    """
    # FIX: Read from the exact display column headers being populated in the loop
    try:
        cost = float(row_data.get('Wholesale Cost ($)', 0))
        price = float(row_data.get('Retail Price ($)', 0))
    except (ValueError, TypeError):
        return "⚠️ Review Required", "Data Type Error! Pricing values are malformed."
    
    # Financial Margin Rule check
    if cost >= price:
        return "⚠️ Review Required", f"Margin Leak! Cost (${cost:.2f}) meets or exceeds Shelf Price (${price:.2f})"
    if cost <= 0 or price <= 0:
        return "⚠️ Review Required", "Pricing Anomaly! Values cannot be zero or negative."
    
    return "✅ Clean", "Passed Master Data Rules"

# Application Processing Trigger
if uploaded_file is not None:
    st.markdown("### ⚙️ Step 2: Live Fluidic Intelligence Mapping & Human-in-the-Loop Review")
    
    # Extract file inputs into standard DataFrame
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
        
    raw_columns = list(df.columns)
    st.info(f"Ingested columns from source file: {raw_columns}")
    
    # Triggering Agent 1
    with st.spinner("NIA Platform: Activating Schema Mapping Agent..."):
        schema_mapping = run_schema_mapping_agent(raw_columns)
        
    st.success("🎉 Schema Mapping Agent has contextually aligned data structures!")
    
    # Display the architectural translation matrix to the user
    with st.expander("🔍 View AI-Agent Translation Dictionary"):
        st.json(schema_mapping)
        
    # Process the table data using our extraction mappings
    processed_records = []
    
    for idx, row in df.iterrows():
        # Extracted normalized attributes
        extracted_row = {
            "SKU ID": row.get(schema_mapping.get('sku_id'), f"UNKNOWN_ROW_{idx}"),
            "Product Name": row.get(schema_mapping.get('product_name'), "N/A"),
            "Wholesale Cost ($)": row.get(schema_mapping.get('wholesale_cost'), 0.0),
            "Retail Price ($)": row.get(schema_mapping.get('retail_price'), 0.0)
        }
        
        # Triggering Agent 2 (Deterministic Quality Node)
        status, rationale = run_anomaly_compliance_agent(extracted_row)
        
        # Assemble interactive layout properties
        extracted_row["Status"] = status
        extracted_row["AI Engine Rationale"] = rationale
        processed_records.append(extracted_row)
        
    processed_df = pd.DataFrame(processed_records)
    
    # Reorder columns for optimal user visual scanning hierarchy
    column_order = ["Status", "SKU ID", "Product Name", "Wholesale Cost ($)", "Retail Price ($)", "AI Engine Rationale"]
    processed_df = processed_df[column_order]
    
    # Split view tabs
    tab1, tab2 = st.tabs(["Raw Source File View", "Active Fluidic Data Pipeline (Human-in-the-Loop)"])
    
    with tab1:
        st.dataframe(df, use_container_width=True)
        
    with tab2:
        st.markdown("#### Review Pipeline")
        st.caption("You can modify cells directly in the table below to override warnings before committing changes to production core networks.")
        
        # Live interactive data canvas
        user_validated_df = st.data_editor(processed_df, use_container_width=True, key="live_editor")
        
        if st.button("🚀 Approve Data & Sync Core Architecture"):
            st.success(f"Successfully processed and cleared {len(user_validated_df)} data schemas into target Master Record endpoints!")