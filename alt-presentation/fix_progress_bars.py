#!/usr/bin/env python3
"""
Fix progress bar percentages to match slide positions.
Handles both inline styles and embedded CSS.
"""

import os
import re
from pathlib import Path

# Progress mapping: slide index → percentage  
PROGRESS_MAP = {
    1: 7, 2: 13, 3: 20, 4: 27, 5: 33, 6: 40, 7: 47, 8: 53,
    9: 60, 10: 67, 11: 73, 12: 80, 13: 87, 14: 93, 15: 100
}

# Slide manifest from navigation.js (1-indexed)
SLIDE_MANIFEST = [
    'page_home/page_home',
    'page_orientation/page_orientation', 
    'page_cast_context/page_cast_context',
    'page_inciting_incident/page_inciting_incident',
    'page_temptations/page_temptations',
    'page_obstacles/page_obstacles',
    'page_core_dilemma/page_core_dilemma',
    'page_turning_point/page_turning_point',
    'page_big_idea/page_big_idea',
    'page_prudent_path/page_prudent_path',
    'page_benefits/page_benefits',
    'page_call_to_action/page_call_to_action',
    'page_future_vision/page_future_vision',
    'page_about_cssi/page_about_cssi',
    'page_references/page_references'
]

def get_slide_index(file_path):
    """Get slide index (1-based) from file path using manifest."""
    file_path_obj = Path(file_path)
    dir_name = file_path_obj.parent.name
    slide_key = f"{dir_name}/{file_path_obj.stem}"
    
    try:
        return SLIDE_MANIFEST.index(slide_key) + 1
    except ValueError:
        return None

def fix_progress_in_file(file_path):
    """Fix progress indicators in a single file."""
    slide_index = get_slide_index(file_path)
    if not slide_index:
        return []
    
    target_percent = PROGRESS_MAP[slide_index]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # Pattern 1: Inline style widths - style="width: NN%"
        def replace_inline_style(match):
            old_percent = int(match.group(1))
            if old_percent != target_percent:
                changes.append(f"Inline style: {old_percent}% → {target_percent}%")
            return f'style="width: {target_percent}%"'
        
        content = re.sub(r'style="width:\s*(\d+)%"', replace_inline_style, content)
        
        # Pattern 2: CSS embedded width properties for progress bars
        def replace_progress_width(match):
            old_percent = int(match.group(1))
            comment_part = match.group(2) if len(match.groups()) >= 2 else ""
            if old_percent != target_percent:
                changes.append(f"CSS progress width: {old_percent}% → {target_percent}%")
            return f'width: {target_percent}%;{comment_part}'
        
        # Look for progress-bar width definitions in CSS
        content = re.sub(
            r'(\s+width:\s*)(\d+)%(;\s*/\*[^*]*\*/)?', 
            lambda m: (
                f'{m.group(1)}{target_percent}%{m.group(3) or ";"}'
                if 'progress' in content[max(0, m.start()-200):m.start()] 
                else m.group(0)
            ),
            content
        )
        
        # More targeted approach for progress-bar class definitions
        lines = content.split('\n')
        in_progress_context = False
        for i, line in enumerate(lines):
            # Track if we're in a progress-related CSS block
            if '.progress-bar' in line or 'progress-fill' in line:
                in_progress_context = True
            elif line.strip().startswith('}'):
                in_progress_context = False
            
            # Replace width percentages in progress context
            if in_progress_context and 'width:' in line and '%' in line:
                width_match = re.search(r'width:\s*(\d+)%;', line)
                if width_match:
                    old_percent = int(width_match.group(1))
                    if old_percent != target_percent:
                        changes.append(f"CSS width: {old_percent}% → {target_percent}%")
                        lines[i] = re.sub(r'width:\s*\d+%;', f'width: {target_percent}%;', line)
        
        content = '\n'.join(lines)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return changes
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

def main():
    """Fix progress indicators for all slides."""
    base_dir = Path('/Users/john/git/cssi-web/alt-presentation')
    
    print("🎯 Fixing progress bar percentages to match slide positions...")
    print(f"📊 Target percentages: {PROGRESS_MAP}")
    print()
    
    total_changes = 0
    files_updated = []
    
    # Process specific slides that need fixing
    slides_to_check = [
        'page_prudent_path/page_prudent_path.html',
        'page_benefits/page_benefits.html', 
        'page_call_to_action/page_call_to_action.html',
        'page_future_vision/page_future_vision.html'
    ]
    
    for slide_file in slides_to_check:
        file_path = base_dir / slide_file
        if file_path.exists():
            changes = fix_progress_in_file(file_path)
            if changes:
                slide_index = get_slide_index(file_path)
                expected_percent = PROGRESS_MAP.get(slide_index, 'Unknown')
                
                print(f"✅ {slide_file} (Slide {slide_index} → {expected_percent}%):")
                for change in changes:
                    print(f"   • {change}")
                
                total_changes += len(changes)
                files_updated.append(str(file_path))
    
    print(f"\n📈 Summary:")
    print(f"   Total changes: {total_changes}")
    print(f"   Files updated: {len(files_updated)}")

if __name__ == '__main__':
    main()