# Crime Status Derivation

## 導出式

罪の重さを把握するための基本的な導出式は以下の数式で導出されます。

- `priority_rate`: 状態の優先度を示す

   - High Priority: $4 \leq PR \leq 5$
   - Moderate Priority: $2 \leq PR < 4$
   - Low Priority: $0 \leq PR < 2$

   $$PR = \frac{\text{Importance of the Crime}}{\text{Total Importance in the Region}}$$

- `guilty_rate`: 罪の程度を示す

   - Highly Guilty: $GR \geq 0.8$
   - Moderately Guilty: $0.5 \leq GR < 0.8$
   - Low Guilt: $0 \leq GR < 0.5$

    $$GR = \frac{\text{Guilty Factors}}{\text{Total Factors}}$$

- `guilty_accuracy`: 罪の正確さを示す

   - High Accuracy: $GA \geq 0.9$
   - Moderate Accuracy: $0.7 \leq GA < 0.9$
   - Low Accuracy: $0 \leq GA < 0.7$

    $$GA = \frac{\text{Guilty Actions Correctly Identified}}{\text{Total Guilty Actions}}$$

- `political_issue`: 政治的問題の影響を示す

   - Significant Political Issue: $PI \geq 0.8$
   - Moderate Political Issue: $0.5 \leq PI < 0.8$
   - Low Political Issue: $0 \leq PI < 0.5$

    $$PI = \frac{\text{Political Implications}}{\text{Total Implications}}$$

- `punishment`: 刑罰の程度を示す

   - Appropriate Punishment: $P \geq 0.7$
   - Moderate Punishment: $0.4 \leq P < 0.7$
   - Lenient Punishment: $0 \leq P < 0.4$

    $$P = \frac{\text{Appropriate Punishment Factors}}{\text{Total Punishment Factors}}$$

- `rally`: 集会やデモの影響を示す

   - High Rally Potential: $RP \geq 0.8$
   - Moderate Rally Potential: $0.5 \leq RP < 0.8$
   - Low Rally Potential: $0 \leq RP < 0.5$

    $$RP = \frac{\text{Potential Support for the Accused}}{\text{Total Potential Support}}$$

- `traceability`: 犯罪の追跡可能性を示す

   - High Traceability: $T \geq 0.9$
   - Moderate Traceability: $0.6 \leq T < 0.9$
   - Low Traceability: $0 \leq T < 0.6$

    $$T = \frac{\text{Evidence Traceability}}{\text{Total Traceable Evidence}}$$

