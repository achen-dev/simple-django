gdjs.CutsceneCode = {};
gdjs.CutsceneCode.GDBub1Objects1= [];
gdjs.CutsceneCode.GDBub1Objects2= [];
gdjs.CutsceneCode.GDBub2Objects1= [];
gdjs.CutsceneCode.GDBub2Objects2= [];
gdjs.CutsceneCode.GDLargeBlockNarrowRectangleObjects1= [];
gdjs.CutsceneCode.GDLargeBlockNarrowRectangleObjects2= [];
gdjs.CutsceneCode.GDBronzeBattleAxeObjects1= [];
gdjs.CutsceneCode.GDBronzeBattleAxeObjects2= [];
gdjs.CutsceneCode.GDBottomColliderObjects1= [];
gdjs.CutsceneCode.GDBottomColliderObjects2= [];
gdjs.CutsceneCode.GDTopColliderObjects1= [];
gdjs.CutsceneCode.GDTopColliderObjects2= [];
gdjs.CutsceneCode.GDMultiDoorObjects1= [];
gdjs.CutsceneCode.GDMultiDoorObjects2= [];
gdjs.CutsceneCode.GDMultiButtonObjects1= [];
gdjs.CutsceneCode.GDMultiButtonObjects2= [];
gdjs.CutsceneCode.GDAlertRadiusObjects1= [];
gdjs.CutsceneCode.GDAlertRadiusObjects2= [];
gdjs.CutsceneCode.GDEnemyGruntObjects1= [];
gdjs.CutsceneCode.GDEnemyGruntObjects2= [];
gdjs.CutsceneCode.GDDebugTextObjects1= [];
gdjs.CutsceneCode.GDDebugTextObjects2= [];
gdjs.CutsceneCode.GDGoalDoorMaskObjects1= [];
gdjs.CutsceneCode.GDGoalDoorMaskObjects2= [];
gdjs.CutsceneCode.GDUITextObjects1= [];
gdjs.CutsceneCode.GDUITextObjects2= [];
gdjs.CutsceneCode.GDTouchButtonObjects1= [];
gdjs.CutsceneCode.GDTouchButtonObjects2= [];
gdjs.CutsceneCode.GDSpeechBubbleObjects1= [];
gdjs.CutsceneCode.GDSpeechBubbleObjects2= [];
gdjs.CutsceneCode.GDLoseTextObjects1= [];
gdjs.CutsceneCode.GDLoseTextObjects2= [];
gdjs.CutsceneCode.GDWinTextObjects1= [];
gdjs.CutsceneCode.GDWinTextObjects2= [];
gdjs.CutsceneCode.GDLoseDesciptionObjects1= [];
gdjs.CutsceneCode.GDLoseDesciptionObjects2= [];
gdjs.CutsceneCode.GDWinDescriptionObjects1= [];
gdjs.CutsceneCode.GDWinDescriptionObjects2= [];
gdjs.CutsceneCode.GDReturnToMenuObjects1= [];
gdjs.CutsceneCode.GDReturnToMenuObjects2= [];
gdjs.CutsceneCode.GDNextLevelObjects1= [];
gdjs.CutsceneCode.GDNextLevelObjects2= [];
gdjs.CutsceneCode.GDRetryLevelObjects1= [];
gdjs.CutsceneCode.GDRetryLevelObjects2= [];
gdjs.CutsceneCode.GDOverlayBackgroundObjects1= [];
gdjs.CutsceneCode.GDOverlayBackgroundObjects2= [];
gdjs.CutsceneCode.GDHealthBarObjects1= [];
gdjs.CutsceneCode.GDHealthBarObjects2= [];
gdjs.CutsceneCode.GDHealthBarBoxObjects1= [];
gdjs.CutsceneCode.GDHealthBarBoxObjects2= [];
gdjs.CutsceneCode.GDBossRobotObjects1= [];
gdjs.CutsceneCode.GDBossRobotObjects2= [];
gdjs.CutsceneCode.GDMenuButtonObjects1= [];
gdjs.CutsceneCode.GDMenuButtonObjects2= [];
gdjs.CutsceneCode.GDNextButtonObjects1= [];
gdjs.CutsceneCode.GDNextButtonObjects2= [];
gdjs.CutsceneCode.GDRetryButtonObjects1= [];
gdjs.CutsceneCode.GDRetryButtonObjects2= [];
gdjs.CutsceneCode.GDPauseButtonObjects1= [];
gdjs.CutsceneCode.GDPauseButtonObjects2= [];
gdjs.CutsceneCode.GDKeyObjects1= [];
gdjs.CutsceneCode.GDKeyObjects2= [];
gdjs.CutsceneCode.GDGoldSquareToggleObjects1= [];
gdjs.CutsceneCode.GDGoldSquareToggleObjects2= [];
gdjs.CutsceneCode.GDExitPauseObjects1= [];
gdjs.CutsceneCode.GDExitPauseObjects2= [];
gdjs.CutsceneCode.GDPauseMenuBackgroundObjects1= [];
gdjs.CutsceneCode.GDPauseMenuBackgroundObjects2= [];
gdjs.CutsceneCode.GDCheckboxObjects1= [];
gdjs.CutsceneCode.GDCheckboxObjects2= [];
gdjs.CutsceneCode.GDCheckbox2Objects1= [];
gdjs.CutsceneCode.GDCheckbox2Objects2= [];
gdjs.CutsceneCode.GDPlayerControlsObjects1= [];
gdjs.CutsceneCode.GDPlayerControlsObjects2= [];
gdjs.CutsceneCode.GDPlayer1PauseTextObjects1= [];
gdjs.CutsceneCode.GDPlayer1PauseTextObjects2= [];
gdjs.CutsceneCode.GDPlayer2PauseTextObjects1= [];
gdjs.CutsceneCode.GDPlayer2PauseTextObjects2= [];
gdjs.CutsceneCode.GDCutsceneVidObjects1= [];
gdjs.CutsceneCode.GDCutsceneVidObjects2= [];

gdjs.CutsceneCode.conditionTrue_0 = {val:false};
gdjs.CutsceneCode.condition0IsTrue_0 = {val:false};
gdjs.CutsceneCode.condition1IsTrue_0 = {val:false};
gdjs.CutsceneCode.conditionTrue_1 = {val:false};
gdjs.CutsceneCode.condition0IsTrue_1 = {val:false};
gdjs.CutsceneCode.condition1IsTrue_1 = {val:false};


gdjs.CutsceneCode.eventsList0 = function(runtimeScene) {

{


gdjs.CutsceneCode.condition0IsTrue_0.val = false;
{
{gdjs.CutsceneCode.conditionTrue_1 = gdjs.CutsceneCode.condition0IsTrue_0;
gdjs.CutsceneCode.conditionTrue_1.val = runtimeScene.getOnceTriggers().triggerOnce(13589660);
}
}if (gdjs.CutsceneCode.condition0IsTrue_0.val) {
{gdjs.evtTools.sound.playSound(runtimeScene, "ea65ea7fc29892eca209efe8b0e1b6c13469698f14d9bdb56e00e23f2466cb6c_Bit Bit Loop.aac", false, 10, 1);
}}

}


{

gdjs.copyArray(runtimeScene.getObjects("CutsceneVid"), gdjs.CutsceneCode.GDCutsceneVidObjects1);

gdjs.CutsceneCode.condition0IsTrue_0.val = false;
{
for(var i = 0, k = 0, l = gdjs.CutsceneCode.GDCutsceneVidObjects1.length;i<l;++i) {
    if ( gdjs.CutsceneCode.GDCutsceneVidObjects1[i].isEnded() ) {
        gdjs.CutsceneCode.condition0IsTrue_0.val = true;
        gdjs.CutsceneCode.GDCutsceneVidObjects1[k] = gdjs.CutsceneCode.GDCutsceneVidObjects1[i];
        ++k;
    }
}
gdjs.CutsceneCode.GDCutsceneVidObjects1.length = k;}if (gdjs.CutsceneCode.condition0IsTrue_0.val) {
{gdjs.evtTools.runtimeScene.replaceScene(runtimeScene, "Level 1", false);
}}

}


{


{
gdjs.copyArray(runtimeScene.getObjects("CutsceneVid"), gdjs.CutsceneCode.GDCutsceneVidObjects1);
{for(var i = 0, len = gdjs.CutsceneCode.GDCutsceneVidObjects1.length ;i < len;++i) {
    gdjs.CutsceneCode.GDCutsceneVidObjects1[i].play();
}
}}

}


};

gdjs.CutsceneCode.func = function(runtimeScene) {
runtimeScene.getOnceTriggers().startNewFrame();

gdjs.CutsceneCode.GDBub1Objects1.length = 0;
gdjs.CutsceneCode.GDBub1Objects2.length = 0;
gdjs.CutsceneCode.GDBub2Objects1.length = 0;
gdjs.CutsceneCode.GDBub2Objects2.length = 0;
gdjs.CutsceneCode.GDLargeBlockNarrowRectangleObjects1.length = 0;
gdjs.CutsceneCode.GDLargeBlockNarrowRectangleObjects2.length = 0;
gdjs.CutsceneCode.GDBronzeBattleAxeObjects1.length = 0;
gdjs.CutsceneCode.GDBronzeBattleAxeObjects2.length = 0;
gdjs.CutsceneCode.GDBottomColliderObjects1.length = 0;
gdjs.CutsceneCode.GDBottomColliderObjects2.length = 0;
gdjs.CutsceneCode.GDTopColliderObjects1.length = 0;
gdjs.CutsceneCode.GDTopColliderObjects2.length = 0;
gdjs.CutsceneCode.GDMultiDoorObjects1.length = 0;
gdjs.CutsceneCode.GDMultiDoorObjects2.length = 0;
gdjs.CutsceneCode.GDMultiButtonObjects1.length = 0;
gdjs.CutsceneCode.GDMultiButtonObjects2.length = 0;
gdjs.CutsceneCode.GDAlertRadiusObjects1.length = 0;
gdjs.CutsceneCode.GDAlertRadiusObjects2.length = 0;
gdjs.CutsceneCode.GDEnemyGruntObjects1.length = 0;
gdjs.CutsceneCode.GDEnemyGruntObjects2.length = 0;
gdjs.CutsceneCode.GDDebugTextObjects1.length = 0;
gdjs.CutsceneCode.GDDebugTextObjects2.length = 0;
gdjs.CutsceneCode.GDGoalDoorMaskObjects1.length = 0;
gdjs.CutsceneCode.GDGoalDoorMaskObjects2.length = 0;
gdjs.CutsceneCode.GDUITextObjects1.length = 0;
gdjs.CutsceneCode.GDUITextObjects2.length = 0;
gdjs.CutsceneCode.GDTouchButtonObjects1.length = 0;
gdjs.CutsceneCode.GDTouchButtonObjects2.length = 0;
gdjs.CutsceneCode.GDSpeechBubbleObjects1.length = 0;
gdjs.CutsceneCode.GDSpeechBubbleObjects2.length = 0;
gdjs.CutsceneCode.GDLoseTextObjects1.length = 0;
gdjs.CutsceneCode.GDLoseTextObjects2.length = 0;
gdjs.CutsceneCode.GDWinTextObjects1.length = 0;
gdjs.CutsceneCode.GDWinTextObjects2.length = 0;
gdjs.CutsceneCode.GDLoseDesciptionObjects1.length = 0;
gdjs.CutsceneCode.GDLoseDesciptionObjects2.length = 0;
gdjs.CutsceneCode.GDWinDescriptionObjects1.length = 0;
gdjs.CutsceneCode.GDWinDescriptionObjects2.length = 0;
gdjs.CutsceneCode.GDReturnToMenuObjects1.length = 0;
gdjs.CutsceneCode.GDReturnToMenuObjects2.length = 0;
gdjs.CutsceneCode.GDNextLevelObjects1.length = 0;
gdjs.CutsceneCode.GDNextLevelObjects2.length = 0;
gdjs.CutsceneCode.GDRetryLevelObjects1.length = 0;
gdjs.CutsceneCode.GDRetryLevelObjects2.length = 0;
gdjs.CutsceneCode.GDOverlayBackgroundObjects1.length = 0;
gdjs.CutsceneCode.GDOverlayBackgroundObjects2.length = 0;
gdjs.CutsceneCode.GDHealthBarObjects1.length = 0;
gdjs.CutsceneCode.GDHealthBarObjects2.length = 0;
gdjs.CutsceneCode.GDHealthBarBoxObjects1.length = 0;
gdjs.CutsceneCode.GDHealthBarBoxObjects2.length = 0;
gdjs.CutsceneCode.GDBossRobotObjects1.length = 0;
gdjs.CutsceneCode.GDBossRobotObjects2.length = 0;
gdjs.CutsceneCode.GDMenuButtonObjects1.length = 0;
gdjs.CutsceneCode.GDMenuButtonObjects2.length = 0;
gdjs.CutsceneCode.GDNextButtonObjects1.length = 0;
gdjs.CutsceneCode.GDNextButtonObjects2.length = 0;
gdjs.CutsceneCode.GDRetryButtonObjects1.length = 0;
gdjs.CutsceneCode.GDRetryButtonObjects2.length = 0;
gdjs.CutsceneCode.GDPauseButtonObjects1.length = 0;
gdjs.CutsceneCode.GDPauseButtonObjects2.length = 0;
gdjs.CutsceneCode.GDKeyObjects1.length = 0;
gdjs.CutsceneCode.GDKeyObjects2.length = 0;
gdjs.CutsceneCode.GDGoldSquareToggleObjects1.length = 0;
gdjs.CutsceneCode.GDGoldSquareToggleObjects2.length = 0;
gdjs.CutsceneCode.GDExitPauseObjects1.length = 0;
gdjs.CutsceneCode.GDExitPauseObjects2.length = 0;
gdjs.CutsceneCode.GDPauseMenuBackgroundObjects1.length = 0;
gdjs.CutsceneCode.GDPauseMenuBackgroundObjects2.length = 0;
gdjs.CutsceneCode.GDCheckboxObjects1.length = 0;
gdjs.CutsceneCode.GDCheckboxObjects2.length = 0;
gdjs.CutsceneCode.GDCheckbox2Objects1.length = 0;
gdjs.CutsceneCode.GDCheckbox2Objects2.length = 0;
gdjs.CutsceneCode.GDPlayerControlsObjects1.length = 0;
gdjs.CutsceneCode.GDPlayerControlsObjects2.length = 0;
gdjs.CutsceneCode.GDPlayer1PauseTextObjects1.length = 0;
gdjs.CutsceneCode.GDPlayer1PauseTextObjects2.length = 0;
gdjs.CutsceneCode.GDPlayer2PauseTextObjects1.length = 0;
gdjs.CutsceneCode.GDPlayer2PauseTextObjects2.length = 0;
gdjs.CutsceneCode.GDCutsceneVidObjects1.length = 0;
gdjs.CutsceneCode.GDCutsceneVidObjects2.length = 0;

gdjs.CutsceneCode.eventsList0(runtimeScene);

return;

}

gdjs['CutsceneCode'] = gdjs.CutsceneCode;
