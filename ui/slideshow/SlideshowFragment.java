package com.example.myapplication.ui.slideshow;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.example.myapplication.R;

public class SlideshowFragment extends Fragment {

    private EditText editTextTemperature, editTextBloodPressureLower, editTextBloodPressureHigher, editTextHeartRate;
    private TextView textViewCategory;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_reading, container, false);

        editTextTemperature = rootView.findViewById(R.id.editTextTemperature);
        editTextBloodPressureLower = rootView.findViewById(R.id.editTextBloodPressureLower);
        editTextBloodPressureHigher = rootView.findViewById(R.id.editTextBloodPressureHigher);
        editTextHeartRate = rootView.findViewById(R.id.editTextHeartRate);
        textViewCategory = rootView.findViewById(R.id.textViewCategory);

        Button buttonAssessReadings = rootView.findViewById(R.id.buttonAssessReadings);
        buttonAssessReadings.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                assessReadings();
            }
        });

        return rootView;
    }

    private void assessReadings() {
        double temperature = Double.parseDouble(editTextTemperature.getText().toString());
        int lowerBloodPressure = Integer.parseInt(editTextBloodPressureLower.getText().toString());
        int higherBloodPressure = Integer.parseInt(editTextBloodPressureHigher.getText().toString());
        int heartRate = Integer.parseInt(editTextHeartRate.getText().toString());

        String category;
        if (temperature <= 37 && lowerBloodPressure < 80 && higherBloodPressure < 120 && heartRate < 160) {
            category = "Normal – no action required";
        } else if ((temperature >= 37 && temperature <= 38) || (lowerBloodPressure >= 80 && lowerBloodPressure <= 110 && higherBloodPressure >= 120 && higherBloodPressure <= 180 && heartRate < 160)) {
            category = "Low risk – notify user to take some measures";
        } else {
            category = "High risk – notify users and send txt to the nurse/GP";
        }

        textViewCategory.setText("Assessment: " + category);
    }
}
