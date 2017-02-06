# Theis_Well_Field_Drawdown
This python script uses scipy functionality (special function + spatial classes) to calculate the drawdown associated with a pumping well field according to the Theis equation. It serves as a simple demo as to how to rapidly process analytical solutions for groundwater flow over a grid. Superposition of the drawdown field onto the interpolated groundwater potentiometric surface can provide insights into the possible impact of well field operation on groundwater flow without having to resort to a more complex numerical model to address larger-scale boundary conditions, property heterogeneities, etc./


The following tab-delimited input files are required:

* params.txt - basic model properties (aquifer characteristics, gridding)
* wells.txt - well locations and pumping rates

More background information can be found here: https://numericalenvironmental.wordpress.com/2017/02/06/rapid-computation-of-groundwater-drawdown-in-a-well-field-via-theis-solution-implemented-with-python-scipy/

Email me with questions at walt.mcnab@gmail.com. 

THIS CODE/SOFTWARE IS PROVIDED IN SOURCE OR BINARY FORM "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
