def should_send_alert(gauge_id, stage_height, last_stage, config):
    """Determine if an alert should be sent for a gauge."""
    stages = config.get("stages", {})
    stage1 = stages.get("stage1")
    stage2 = stages.get("stage2")
    if stage2 is not None and stage_height > stage2:
        return last_stage != "stage2", "FLOOD STAGE2 WARNING"
    elif stage1 is not None and stage_height > stage1:
        return last_stage != "stage1", "FLOOD STAGE1 WARNING"
    elif stage1 is not None and stage_height <= stage1:
        return last_stage in ("stage1", "stage2"), "FLOOD ALL-CLEAR"
    return False, None
