package com.example.myapplication.ui.gallery;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.util.TypedValue;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.example.myapplication.R;

import java.util.Arrays;

public class GalleryFragment extends Fragment {

    private TextView textGallery;
    private Spinner dropDownMenu;
    private Button changeFontSizeButton;
    private Button changeFontStyleButton;


    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_gallery, container, false);

        textGallery = rootView.findViewById(R.id.text_gallery);
        dropDownMenu = rootView.findViewById(R.id.dropDownMenu);
        changeFontSizeButton = rootView.findViewById(R.id.changeFontSizeButton);
        changeFontStyleButton = rootView.findViewById(R.id.changeFontStyleButton);


        // Populate the dropdown menu with options
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(requireContext(), R.array.text_options_array, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        dropDownMenu.setAdapter(adapter);

        changeFontSizeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Show a dialog with options for font sizes
                AlertDialog.Builder builder = new AlertDialog.Builder(requireContext());
                builder.setTitle("Select Font Size");

                // Define an array of font size options
                final String[] fontSizeOptions = {"Small", "Medium", "Large"};

                // Set the font size options as items in the dialog
                builder.setItems(fontSizeOptions, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        // Set the font size based on the selected option
                        switch (which) {
                            case 0:
                                textGallery.setTextSize(TypedValue.COMPLEX_UNIT_SP, 16); // Small
                                break;
                            case 1:
                                textGallery.setTextSize(TypedValue.COMPLEX_UNIT_SP, 20); // Medium
                                break;
                            case 2:
                                textGallery.setTextSize(TypedValue.COMPLEX_UNIT_SP, 24); // Large
                                break;
                        }
                    }
                });

                // Display the dialog
                builder.show();
            }
        });

        changeFontStyleButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder builder = new AlertDialog.Builder(requireContext());
                builder.setTitle("Select Font Style");
                String[] fontStyleOptions = {"Normal", "Italic", "Bold"};
                builder.setItems(fontStyleOptions, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        int newStyle = Typeface.NORMAL;
                        switch (which) {
                            case 0: // Normal
                                newStyle = Typeface.NORMAL;
                                break;
                            case 1: // Italic
                                newStyle = Typeface.ITALIC;
                                break;
                            case 2: // Bold
                                newStyle = Typeface.BOLD;
                                break;
                        }
                        textGallery.setTypeface(null, newStyle);
                    }
                });
                builder.show();
            }
        });

        return rootView;
    }
}
