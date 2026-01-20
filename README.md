# Voice for the Voiceless 🎤

> “Imagine being in pain, scared, or frustrated — and having no way to tell anyone.”

## Problem
Millions of non-verbal individuals (autism, cerebral palsy, stroke recovery, ALS)
experience emotions but cannot clearly express them to caregivers, leading to
miscommunication and delayed care.

## Solution
Voice for the Voiceless is a lightweight AI system that detects emotion from
vocal sounds (cries, hums, non-verbal noises) and provides instant feedback
to caregivers — even on low-cost, offline devices.

## Technical Approach
We compare two architectures:

### Baseline Model
- Standard neural network
- Larger size
- Slower inference

### Dendritic-Optimized Model
- Inspired by dendritic signal processing
- Smaller internal representations
- Faster inference with improved accuracy

## Optimization Results
- ~52% reduction in model size
- ~44% faster inference
- Slight accuracy improvement

## Dataset
Architecture designed based on CREMA-D emotion dataset characteristics.
This demo focuses on inference and optimization clarity; full-scale training
is planned.

## Impact
- Improves quality of care for non-verbal individuals
- Works on low-cost Android devices
- Privacy-safe (offline inference)
- Reduces cost compared to specialized hardware

## Tech Stack
- PyTorch
- Streamlit
- Dendritic-inspired optimization

Built for the **Perforated AI Hackathon**.
