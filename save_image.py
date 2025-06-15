import os
import matplotlib.pyplot as plt

def plot_and_save_membership_functions(
    x_ph, ph_acidic, ph_neutral, ph_alkali,
    x_tds, tds_lowest, tds_low, tds_medium, tds_high,
    x_temp, temp_cold, temp_normal, temp_hot,
    x_output, output_not_normal, output_normal,
    output_dir='images/membership_functions', width=6, height=4
):
    os.makedirs(output_dir, exist_ok=True)
    y_label = 'Membership Degree'

    # pH plot
    plt.figure(figsize=(width, height))
    plt.plot(x_ph, ph_acidic, label='Acidic', color='blue')
    plt.plot(x_ph, ph_neutral, label='Optimal', color='green')
    plt.plot(x_ph, ph_alkali, label='Alkaline', color='red')
    plt.xlabel('pH')
    plt.ylabel(y_label)
    plt.title('Acidity Level (pH)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'ph_membership.png'))
    plt.show()
    plt.close()

    # TDS plot
    plt.figure(figsize=(width, height))
    plt.plot(x_tds, tds_lowest, label='Very Low', color='blue')
    plt.plot(x_tds, tds_low, label='Low', color='orange')
    plt.plot(x_tds, tds_medium, label='Optimal', color='green')
    plt.plot(x_tds, tds_high, label='High', color='red')
    plt.xlabel('TDS (ppm)')
    plt.ylabel(y_label)
    plt.title('Total Dissolved Solids (TDS)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tds_membership.png'))
    plt.show()
    plt.close()

    # Water Temperature plot
    plt.figure(figsize=(width, height))
    plt.plot(x_temp, temp_cold, label='Cold', color='blue')
    plt.plot(x_temp, temp_normal, label='Optimal', color='green')
    plt.plot(x_temp, temp_hot, label='Hot', color='red')
    plt.xlabel('Water Temperature (°C)')
    plt.ylabel(y_label)
    plt.title('Water Temperature')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'temp_membership.png'))
    plt.show()
    plt.close()

    # Output Condition plot
    plt.figure(figsize=(width, height))
    plt.plot(x_output, output_not_normal, label='Abnormal', color='red')
    plt.plot(x_output, output_normal, label='Normal', color='green')
    plt.xlabel('Environment Condition')
    plt.ylabel(y_label)
    plt.title('Environment Condition')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'output_membership.png'))
    plt.show()
    plt.close()

    export_input_membership_subplot(
        x_ph, ph_acidic, ph_neutral, ph_alkali,
        x_tds, tds_lowest, tds_low, tds_medium, tds_high,
        x_temp, temp_cold, temp_normal, temp_hot,
        output_dir="images/"
    )


def export_input_membership_subplot(
    x_ph, ph_acidic, ph_neutral, ph_alkali,
    x_tds, tds_lowest, tds_low, tds_medium, tds_high,
    x_temp, temp_cold, temp_normal, temp_hot,
    output_dir='images/membership_functions', width=6, height=12
):
    os.makedirs(output_dir, exist_ok=True)
    y_label = 'Membership Degree'

    fig, axes = plt.subplots(3, 1, figsize=(width, height))

    # pH subplot
    axes[0].plot(x_ph, ph_acidic, label='Acid', color='blue')
    axes[0].plot(x_ph, ph_neutral, label='Optimal', color='green')
    axes[0].plot(x_ph, ph_alkali, label='Alkaline', color='red')
    axes[0].set_xlabel('pH')
    axes[0].set_ylabel(y_label)
    axes[0].set_title('Acidity Level (pH)')
    axes[0].legend()
    axes[0].grid(True)

    # TDS subplot
    axes[1].plot(x_tds, tds_lowest, label='Lower', color='blue')
    axes[1].plot(x_tds, tds_low, label='Low', color='orange')
    axes[1].plot(x_tds, tds_medium, label='Optimal', color='green')
    axes[1].plot(x_tds, tds_high, label='High', color='red')
    axes[1].set_xlabel('TDS (ppm)')
    axes[1].set_ylabel(y_label)
    axes[1].set_title('Total Dissolved Solids (TDS)')
    axes[1].legend()
    axes[1].grid(True)

    # Water Temperature subplot
    axes[2].plot(x_temp, temp_cold, label='Cold', color='blue')
    axes[2].plot(x_temp, temp_normal, label='Optimal', color='green')
    axes[2].plot(x_temp, temp_hot, label='Hot', color='red')
    axes[2].set_xlabel('Water Temperature (°C)')
    axes[2].set_ylabel(y_label)
    axes[2].set_title('Water Temperature')
    axes[2].legend()
    axes[2].grid(True)

    plt.tight_layout()
    save_path = os.path.join(output_dir, 'input_membership_subplot.png')
    plt.savefig(save_path)
    plt.close()