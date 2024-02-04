import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


# We'll use this interpolation to rebuild an analogue signal from digital samples
# credit for this implementation goes to endolith: https://gist.github.com/endolith
def sinc_interp(x, s, u):
    """
    Interpolates x, sampled at "s" instants
    Output y is sampled at "u" instants ("u" for "upsampled")
    
    from Matlab:
    http://phaseportrait.blogspot.com/2008/06/sinc-interpolation-in-matlab.html        
    """
    # Validate arguments
    if len(x) != len(s):
        raise(Exception, 'x and s must be the same length')
    
    # Find the period    
    T = s[1] - s[0]    
    
    transposed = np.transpose(np.tile(np.arange(len(s)), (len(u),1))) * T    
    
    sincM = np.tile(u, (len(s), 1)) - transposed
    y = np.dot(x, np.sinc(sincM / T))
    
    return y
        

#Set up figure
fig, axes = plt.subplots(3,4,figsize=(12,4),sharex='col',sharey='row')

# The signal will be a pure sinusoidal, at a frequency of 3 Hz (Hertz, Hz = 1/s)
frequency = 3;
# A high sampling rate (number of recorded data points per time unit) will give the
# illusion of an analog signal, you will not be able to see the time steps.
# At a lower sampling rate, you can clearly see when a point was sampled
# If the sampling rate is at or below the Nyquist frequency, the acquired signal will be erroneous.

# Now lets discretize this with a sampling rate of 10 Hz

# We'll look at a dozen frequencies
sampling_rates = [50,25,12,7,6.2,6,5.8,5,4.5,4,3,2.9];#np.logspace(np.log10(96),np.log10(1.5),num=8);

# Compare all signals to a sampling rate of 50 Hz. Used by the interpolation
reference_sampling_rate = 50;
reference_time = np.arange(-10,10,1/reference_sampling_rate);
reference_time = np.append(reference_time,1);
reference_voltage = np.sin(2*np.pi*frequency*reference_time)

# Iterate over axes and sampling rates
for (axe,sampling_rate) in zip(axes.reshape(-1),sampling_rates):
    # Create the time vector.
    time = np.arange(-10.01,10,1/sampling_rate);
    
    # Compute the sinusoidal (x = Amplitude*sin(angular_frequency * time))
    # Where angular_frequency = 2 * pi * frequency
    voltage  =  np.sin(2*np.pi*frequency*time);
    
    # In order to get a better idea of the signal represented by the samples it is interpolated
    # and plotted on top of the discretized signal. this step is not part of discretization.
    # interpolate the signal using Whittaker-Shannon Interpolation
    interpolated_voltage = sinc_interp(voltage,time,reference_time);
    
    axe.stem(time,voltage,use_line_collection=True);
    axe.plot(reference_time,interpolated_voltage,'r');
    axe.plot(reference_time,reference_voltage,'g.')
    axe.set_title('Sampling Rate = {:05.2f} Hz'.format(sampling_rate))
    axe.set_xlim(0,1)
    
plt.show()
plt.tight_layout()