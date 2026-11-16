# Canonical Mathematical Formulations, Operator Models & Scaling Bounds (`mathematical_models_and_scaling.md`)

> **Empirical Basis**: Distilled from published `llm_read` papers and verified referee comments (`C14` Mathematical Model Rigour, `C4` Scaling & Loss Bounds, `C2` Energy Amortization). Use these equations in Main Text `Results` and `Supplementary Notes` to pre-empt theory and physics referees.

---

## 1. Coherent MZI Meshes & Non-Unitary SVD Processors (`MZI`)

1. **Single $2\times 2$ Mach–Zehnder Interferometer Transfer Matrix**:
   For an MZI with internal phase shifter $\theta \in [0, \pi]$, external phase shifter $\phi \in [0, 2\pi)$, and imperfect directional coupler splitting ratios $\alpha_1, \alpha_2 \in (-\frac{\pi}{4}, \frac{\pi}{4})$ around ideal $50:50$:
   $$\mathbf{T}_{\text{MZI}}(\theta, \phi) = i e^{i\theta/2} \begin{pmatrix} e^{i\phi}(\sin\frac{\theta}{2}\cos 2\epsilon - \cos\frac{\theta}{2}\sin 2\epsilon) & e^{i\phi}(\cos\frac{\theta}{2}\cos 2\delta + i\sin\frac{\theta}{2}\sin 2\delta) \\ \cos\frac{\theta}{2}\cos 2\delta - i\sin\frac{\theta}{2}\sin 2\delta & -\sin\frac{\theta}{2}\cos 2\epsilon - \cos\frac{\theta}{2}\sin 2\epsilon \end{pmatrix}$$
   where $\epsilon = (\alpha_1 + \alpha_2)/2$ (common-mode splitting error) and $\delta = (\alpha_1 - \alpha_2)/2$ (differential splitting error), bounding the achievable extinction ratio to $\text{ER}_{\max} \approx -20\log_{10}(\sin 2|\epsilon|)\text{ dB}$ (`Nature Photonics_17V11_441` Shen; `Science_23V380_398` Pai).
2. **Arbitrary $N\times M$ Matrix via Singular Value Decomposition (SVD)**:
   $$\mathbf{W} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\dagger, \qquad \mathbf{U} = \mathbf{D} \prod_{(m,n)\in\mathcal{S}_U} \mathbf{T}_{m,n}(\theta_{mn}, \phi_{mn})$$
   where $\mathcal{S}_U$ has $N(N-1)/2$ MZIs in rectangular (`Clements`) or triangular (`Reck`) topology.
3. **Matrix Fidelity Metric (`C11` / `C14` Standard)**:
   $$F(\mathbf{U}_{\text{target}}, \mathbf{U}_{\text{meas}}) = \left| \frac{\text{Tr}(\mathbf{U}_{\text{target}}^\dagger \mathbf{U}_{\text{meas}})}{\sqrt{\text{Tr}(\mathbf{U}_{\text{target}}^\dagger \mathbf{U}_{\text{target}})\,\text{Tr}(\mathbf{U}_{\text{meas}}^\dagger \mathbf{U}_{\text{meas}})}} \right|^2 \in [0, 1]$$

---

## 2. Microring Resonator (`MRR`) Weight Banks & Thermal Crosstalk Compensation

1. **All-Pass & Add-Drop Coupled-Mode Transmission**:
   For an add-drop microring with round-trip amplitude transmission $a = e^{-\alpha L_{\text{rt}}/2}$, self-coupling coefficients $r_1, r_2$, and round-trip phase $\phi(\lambda, V, T) = \frac{2\pi}{\lambda} n_{\text{eff}}(V, T) L_{\text{rt}}$:
   $$T_{\text{thru}}(\phi) = \frac{r_2^2 a^2 - 2 r_1 r_2 a \cos\phi + r_1^2}{1 - 2 r_1 r_2 a \cos\phi + (r_1 r_2 a)^2}, \qquad T_{\text{drop}}(\phi) = \frac{(1 - r_1^2)(1 - r_2^2) a}{1 - 2 r_1 r_2 a \cos\phi + (r_1 r_2 a)^2}$$
2. **Balanced Differential Photodetection Weighting**:
   For WDM channel $\lambda_i$, the signed synaptic weight $w_i \in [-1, +1]$ is obtained from the differential photocurrent between drop and through ports:
   $$w_i(\Delta\lambda_i) = T_{\text{drop}}(\lambda_i; \Delta\lambda_i) - T_{\text{thru}}(\lambda_i; \Delta\lambda_i)$$
3. **Thermal Crosstalk Compensation Matrix**:
   For an array of $N$ microrings with mutual thermal impedance matrix $\mathbf{R}_{\text{th}} \in \mathbb{R}^{N\times N}$, the target resonance detuning vector $\Delta\boldsymbol{\lambda}_{\text{target}}$ is achieved by solving the pre-compensated power vector $\mathbf{P} = \mathbf{R}_{\text{th}}^{-1} (\Delta\boldsymbol{\lambda}_{\text{target}} / \eta_{\text{TO}})$ subject to $P_i \ge 0$ (`Nature_22V606_501` Ashtiani; `Nature_26V651_927` Ashtiani).

---

## 3. Non-Volatile Phase-Change Photonic Synapses (`PCM`)

1. **Complex Refractive Index Perturbation Along Waveguide Length $L_{\text{PCM}}$**:
   Switching a chalcogenide patch ($\text{GST}$, $\text{GSST}$, $\text{Sb}_2\text{Se}_3$, or $\text{Sb}_2\text{S}_3$) with crystalline fraction $c \in [0, 1]$ modifies both modal effective index and modal attenuation (`Nature_19V569_208` Feldmann; `Nature_21V589_52` Feldmann; `Nature Photonics_21V15_541` Delaney):
   $$n_{\text{eff}}(c) = n_{\text{eff}, 0} + c\,\Delta n_{\text{eff}}, \qquad \alpha_{\text{mod}}(c) = \alpha_0 + c\,\Delta\alpha_{\text{mod}}, \qquad \text{FOM}_{\text{PCM}} = \frac{\Delta n}{\Delta k}$$
   The complex transmission of a waveguide/ring section of length $L_{\text{PCM}}$ is $t(c) = \exp\!\big(-(\alpha_0 + c\Delta\alpha_{\text{mod}})L_{\text{PCM}}/2 - i \frac{2\pi}{\lambda}(n_{\text{eff},0} + c\Delta n_{\text{eff}})L_{\text{PCM}}\big)$.

---

## 4. Fundamental Scaling Bounds: Noise-Limited ENOB & Energy Amortization Crossover (`C2`, `C4`, `C8`)

1. **Photodetector SNR & Effective Number of Bits (`ENOB`) Ceiling**:
   For detected optical power $P_{\text{det}}$, photodetector responsivity $\mathcal{R}\text{ [A/W]}$, electrical bandwidth $B$, Laser Relative Intensity Noise ($\text{RIN}\text{ [dBc/Hz]}$), shot noise, and TIA thermal noise current density $i_{\text{th}}\text{ [A/}\sqrt{\text{Hz}}\text{]}$:
   $$\text{SNR}_{\text{elec}} = \frac{(\mathcal{R} P_{\text{det}})^2}{\left( 2 q \mathcal{R} P_{\text{det}} + \text{RIN}\cdot (\mathcal{R} P_{\text{det}})^2 + i_{\text{th}}^2 \right) B}, \qquad \text{ENOB}_{\max} = \frac{10\log_{10}(\text{SNR}_{\text{elec}}) - 1.76}{6.02}$$
   *Referee Check*: Any paper claiming $\ge 8\text{ bits}$ at $\ge 10\text{ GHz}$ must prove that $P_{\text{det}}$ and $\text{RIN}$ satisfy $\text{SNR}_{\text{elec}} > 50\text{ dB}$ after subtracting chip insertion loss $\text{IL}_{\text{dB}}$ (`Nature_25V640_368` Ahmed; `Science_23V379_41` Miller).
2. **Optical vs. Electronic Energy Amortization Crossover Dimension $N^*$**:
   For an $N\times N$ matrix–vector multiplication where input encoding requires $N$ DAC/modulator operations ($E_{\text{DAC+mod}}$ per element), output readout requires $N$ TIA/ADC operations ($E_{\text{TIA+ADC}}$ per element), static holding/laser power is $P_{\text{static}}$ at clock rate $f_{\text{clk}}$, and a digital CMOS MAC costs $E_{\text{MAC, dig}}$:
   $$E_{\text{tot, opt}}(N) = N \cdot E_{\text{DAC+mod}} + N \cdot E_{\text{TIA+ADC}} + \frac{P_{\text{static}}}{f_{\text{clk}}} < N^2 \cdot E_{\text{MAC, dig}}$$
   Solving for the minimum matrix dimension $N^*$ where photonic $O(N)$ conversion overhead is amortized below digital $O(N^2)$ compute energy:
   $$N^* > \frac{E_{\text{DAC+mod}} + E_{\text{TIA+ADC}}}{2 E_{\text{MAC, dig}}} + \sqrt{\left(\frac{E_{\text{DAC+mod}} + E_{\text{TIA+ADC}}}{2 E_{\text{MAC, dig}}}\right)^2 + \frac{P_{\text{static}}}{f_{\text{clk}} E_{\text{MAC, dig}}}}$$
   Including this exact crossover plot or equation in Discussion/SI (`Nature_25V645_53` Momeni; `Science_22V378_270` Sludds) neutralizes `C2` and `C8` energy objections immediately.
